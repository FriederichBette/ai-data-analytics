import os
import re
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

# Load environment variables
load_dotenv()

app = FastAPI(title="LLM Data Analytics Backend")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
# WICHTIG: Du brauchst den "Direct Connection String" von Supabase Settings -> Database -> Connection String -> URI
DATABASE_URL = os.getenv("DATABASE_URL") 
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma2:2b") # Default fallback

# System Prompt: Hier erklären wir dem LLM die Datenbank
SYSTEM_PROMPT = """
You are a PostgreSQL expert. Your job is to translate natural language questions into executable SQL queries.
You must ONLY output the SQL query. Do not add any markdown, explanation, or notes.

The database schema is as follows:

Table: public.transactions
Columns:
- id (uuid)
- amount (decimal) - Negative values usually mean expenses, but check context.
- category (text) - e.g. 'Miete', 'Lebensmittel', 'Gehalt'
- description (text)
- date (date)

Rules:
1. Return ONLY valid SQL.
2. Use valid PostgreSQL syntax.
3. If the user asks for "Ausgaben" (expenses), look for amounts.
4. Do not delete or modify data, only SELECT.
"""

class QueryRequest(BaseModel):
    natural_language_query: str

class QueryResponse(BaseModel):
    sql_query: str
    data: list
    error: str | None = None

def get_db_connection():
    if not DATABASE_URL:
        raise Exception("DATABASE_URL is missing in .env")
    return psycopg2.connect(DATABASE_URL)

def clean_sql(llm_response: str) -> str:
    """Removes markdown code blocks and extra text from LLM response"""
    # Remove ```sql ... ```
    clean = re.sub(r'```sql\s*', '', llm_response, flags=re.IGNORECASE)
    clean = re.sub(r'```', '', clean)
    # Entferne Whitespace vorne/hinten
    return clean.strip()

@app.get("/")
def read_root():
    return {"status": "online", "model": OLLAMA_MODEL}

@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    try:
        print(f"Received query: {request.natural_language_query}")
        
        # 1. Construct Prompt
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser Question: {request.natural_language_query}\nSQL Query:"
        
        # 2. Call Ollama
        llm_result = ""
        try:
            async with httpx.AsyncClient(timeout=120.0) as client:
                print(f"Connecting to Ollama at {OLLAMA_URL}...")
                response = await client.post(
                    OLLAMA_URL,
                    json={
                        "model": OLLAMA_MODEL,
                        "prompt": full_prompt,
                        "stream": False,
                        "options": {"temperature": 0.1}
                    }
                )
                if response.status_code != 200:
                    raise Exception(f"Ollama Error {response.status_code}: {response.text}")
                
                llm_result = response.json().get("response", "")
                print(f"LLM Raw Output: {llm_result}")
                
        except Exception as e:
            # Log specific Ollama error
            with open("ollama_error.log", "w") as f:
                f.write(str(e))
            raise HTTPException(status_code=500, detail=f"Ollama Fail: {str(e)}")

        # 3. Clean SQL
        sql_query = clean_sql(llm_result)
        print(f"Cleaned SQL: {sql_query}")
        
        # 4. Execute SQL
        data = []
        error_msg = None
        
        try:
            conn = get_db_connection()
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute(sql_query)
            data = cur.fetchall()
            cur.close()
            conn.close()
        except psycopg2.OperationalError as e:
            error_msg = f"DB Connection Error: {str(e)}"
        except Exception as e:
            error_msg = f"SQL Error: {str(e)}"

        return {
            "sql_query": sql_query,
            "data": data,
            "error": error_msg
        }

    except Exception as e:
        # GLOBAL CRASH HANDLER
        import traceback
        error_trace = traceback.format_exc()
        with open("backend_crash.log", "w") as f:
            f.write(error_trace)
        print("CRASH DETECTED!")
        raise HTTPException(status_code=500, detail=f"CRASH: {str(e)}")

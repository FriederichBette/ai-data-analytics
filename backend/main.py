"""
FastAPI Backend für Data Analytics LLM System
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import os
from dotenv import load_dotenv

from llm.text_to_sql import TextToSQLEngine
from api.database import DatabaseManager

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Data Analytics LLM API",
    description="Natürlichsprachliche Datenbank-Abfragen mit LLM",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
db_manager = DatabaseManager()
text_to_sql = TextToSQLEngine()


class QueryRequest(BaseModel):
    """Request model for natural language queries"""
    query: str
    max_rows: Optional[int] = 100


class QueryResponse(BaseModel):
    """Response model for query results"""
    success: bool
    sql_query: Optional[str] = None
    data: Optional[List[Dict[str, Any]]] = None
    error: Optional[str] = None
    row_count: Optional[int] = None


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "service": "Data Analytics LLM API",
        "version": "1.0.0"
    }


@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "database": "connected" if db_manager.is_connected() else "disconnected",
        "llm_provider": os.getenv("LLM_PROVIDER", "not_configured")
    }


@app.post("/query", response_model=QueryResponse)
async def execute_natural_language_query(request: QueryRequest):
    """
    Execute a natural language query against the database
    
    Example:
    {
        "query": "Zeige mir die Top 10 Verkäufe im August sortiert nach Umsatz"
    }
    """
    try:
        # Convert natural language to SQL
        sql_query = await text_to_sql.generate_sql(request.query)
        
        if not sql_query:
            raise HTTPException(
                status_code=400,
                detail="Konnte keine SQL-Abfrage aus der Eingabe generieren"
            )
        
        # Execute SQL query
        results = await db_manager.execute_query(sql_query, max_rows=request.max_rows)
        
        return QueryResponse(
            success=True,
            sql_query=sql_query,
            data=results,
            row_count=len(results)
        )
        
    except Exception as e:
        return QueryResponse(
            success=False,
            error=str(e)
        )


@app.get("/schema")
async def get_database_schema():
    """Get the current database schema for reference"""
    try:
        schema = await db_manager.get_schema_info()
        return {
            "success": True,
            "schema": schema
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/tables")
async def list_tables():
    """List all available tables in the database"""
    try:
        tables = await db_manager.list_tables()
        return {
            "success": True,
            "tables": tables
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("BACKEND_PORT", 8000))
    host = os.getenv("BACKEND_HOST", "0.0.0.0")
    
    print(f"🚀 Starting Data Analytics LLM API on {host}:{port}")
    print(f"📊 LLM Provider: {os.getenv('LLM_PROVIDER', 'not configured')}")
    
    uvicorn.run("main:app", host=host, port=port, reload=True)

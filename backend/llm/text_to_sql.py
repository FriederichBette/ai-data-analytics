import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class TextToSQLEngine:
    def __init__(self):
        self.provider = os.getenv("LLM_PROVIDER", "ollama").lower()
        self.schema_context = self._build_schema_context()
        self.client = None # WICHTIG: Immer initialisieren!
        
        if self.provider == "openai":
            self._init_openai()
        elif self.provider == "ollama":
            self._init_ollama()
    
    def _init_ollama(self):
        try:
            import requests
            self.ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
            self.model = os.getenv("OLLAMA_MODEL", "gemma2:2b")
            
            response = requests.get(f"{self.ollama_url}/api/tags", timeout=2)
            if response.status_code == 200:
                print(f"? Ollama connected with model: {self.model}")
                self.client = True # Client erfolgreich!
            else:
                print("?? Ollama not available")
        except Exception as e:
            print(f"?? Ollama initialization failed: {e}")
            self.client = None # Fallback

    def _build_schema_context(self) -> str:
        return """Du bist ein SQL-Experte. Generiere PostgreSQL-Queries basierend auf dem folgenden Schema:
TABELLEN:
1. sales (id, product_id, customer_id, quantity, total_amount, sale_date)
2. products (id, name, category, price, cost, margin)
3. customers (id, name, email, country, city)
Generiere NUR den SQL Code."""
    
    async def generate_sql(self, natural_language_query: str) -> Optional[str]:
        if not self.client:
            return self._get_demo_query(natural_language_query)
            
        try:
            import requests
            prompt = f"{self.schema_context}\n\nUser Query: {natural_language_query}\n\nSQL Query:"
            
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {"temperature": 0.1}
                },
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                sql = result.get("response", "").strip().replace("`sql", "").replace("`", "").strip()
                return sql
            return self._get_demo_query(natural_language_query)
                
        except Exception as e:
            print(f"Error: {e}")
            return self._get_demo_query(natural_language_query)

    def _get_demo_query(self, query: str) -> str:
        q = query.lower()
        if "top" in q: return "SELECT * FROM sales ORDER BY total_amount DESC LIMIT 10"
        if "produkt" in q: return "SELECT * FROM products LIMIT 10"
        if "kunde" in q: return "SELECT * FROM customers LIMIT 10"
        return "SELECT * FROM sales LIMIT 5"

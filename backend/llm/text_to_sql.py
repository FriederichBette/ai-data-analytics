"""
Text-to-SQL Engine mit Unterstützung für OpenAI und Ollama
"""
import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class TextToSQLEngine:
    """Converts natural language queries to SQL using LLM"""
    
    def __init__(self):
        self.provider = os.getenv("LLM_PROVIDER", "ollama").lower()
        self.schema_context = self._build_schema_context()
        
        if self.provider == "openai":
            self._init_openai()
        elif self.provider == "ollama":
            self._init_ollama()
        else:
            raise ValueError(f"Unsupported LLM provider: {self.provider}")
    
    def _init_openai(self):
        """Initialize OpenAI client"""
        try:
            from openai import OpenAI
            self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
            print(f"✅ OpenAI initialized with model: {self.model}")
        except Exception as e:
            print(f"⚠️  OpenAI initialization failed: {e}")
            self.client = None
    
    def _init_ollama(self):
        """Initialize Ollama client"""
        try:
            import requests
            self.ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
            self.model = os.getenv("OLLAMA_MODEL", "llama3")
            
            # Test connection
            response = requests.get(f"{self.ollama_url}/api/tags", timeout=2)
            if response.status_code == 200:
                print(f"✅ Ollama connected with model: {self.model}")
            else:
                print("⚠️  Ollama not available")
                self.client = None
        except Exception as e:
            print(f"⚠️  Ollama initialization failed: {e}")
            print("💡 Tipp: Starte Ollama mit 'ollama serve' oder füge OpenAI Key hinzu")
            self.client = None
    
    def _build_schema_context(self) -> str:
        """Build database schema context for LLM"""
        return """
Du bist ein SQL-Experte. Generiere PostgreSQL-Queries basierend auf dem folgenden Schema:

TABELLEN:

1. sales (Verkäufe)
   - id: integer (Primary Key)
   - product_id: integer (Foreign Key -> products.id)
   - customer_id: integer (Foreign Key -> customers.id)
   - quantity: integer (Anzahl verkaufter Einheiten)
   - total_amount: decimal (Gesamtumsatz in EUR)
   - sale_date: date (Verkaufsdatum)
   - created_at: timestamp

2. products (Produkte)
   - id: integer (Primary Key)
   - name: varchar (Produktname)
   - category: varchar (Kategorie: Electronics, Clothing, Food, etc.)
   - price: decimal (Verkaufspreis in EUR)
   - cost: decimal (Einkaufspreis in EUR)
   - margin: decimal (Gewinnmarge in %)
   - created_at: timestamp

3. customers (Kunden)
   - id: integer (Primary Key)
   - name: varchar (Kundenname)
   - email: varchar (E-Mail)
   - country: varchar (Land)
   - city: varchar (Stadt)
   - created_at: timestamp

WICHTIGE REGELN:
- Generiere NUR die SQL-Query, keine Erklärungen
- Nutze JOINs wenn mehrere Tabellen benötigt werden
- Nutze deutsche Monatsnamen wenn erwähnt (z.B. August = Monat 8)
- Sortiere mit ORDER BY wenn "sortiert" erwähnt wird
- Limitiere Ergebnisse mit LIMIT wenn "Top X" erwähnt wird
- Nutze aggregierte Funktionen (SUM, AVG, COUNT) für Berechnungen
"""
    
    async def generate_sql(self, natural_language_query: str) -> Optional[str]:
        """
        Generate SQL query from natural language
        
        Args:
            natural_language_query: User's question in natural language
            
        Returns:
            SQL query string or None if generation fails
        """
        if self.provider == "openai":
            return await self._generate_with_openai(natural_language_query)
        elif self.provider == "ollama":
            return await self._generate_with_ollama(natural_language_query)
        else:
            return None
    
    async def _generate_with_openai(self, query: str) -> Optional[str]:
        """Generate SQL using OpenAI"""
        if not self.client:
            return None
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.schema_context},
                    {"role": "user", "content": f"Generiere eine SQL-Query für: {query}"}
                ],
                temperature=0.1,
                max_tokens=500
            )
            
            sql_query = response.choices[0].message.content.strip()
            # Remove markdown code blocks if present
            sql_query = sql_query.replace("```sql", "").replace("```", "").strip()
            
            return sql_query
            
        except Exception as e:
            print(f"OpenAI error: {e}")
            return None
    
    async def _generate_with_ollama(self, query: str) -> Optional[str]:
        """Generate SQL using Ollama"""
        if not self.client:
            # Return a fallback demo query if Ollama is not available
            return self._get_demo_query(query)
        
        try:
            import requests
            
            prompt = f"{self.schema_context}\n\nUser Query: {query}\n\nSQL Query:"
            
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.1
                    }
                },
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                sql_query = result.get("response", "").strip()
                # Clean up the response
                sql_query = sql_query.replace("```sql", "").replace("```", "").strip()
                return sql_query
            else:
                return self._get_demo_query(query)
                
        except Exception as e:
            print(f"Ollama error: {e}")
            return self._get_demo_query(query)
    
    def _get_demo_query(self, query: str) -> str:
        """Return a demo query when LLM is not available"""
        query_lower = query.lower()
        
        # Simple keyword matching for demo purposes
        if "top" in query_lower and "verkäufe" in query_lower:
            return """
SELECT s.id, p.name, c.name as customer, s.quantity, s.total_amount, s.sale_date
FROM sales s
JOIN products p ON s.product_id = p.id
JOIN customers c ON s.customer_id = c.id
ORDER BY s.total_amount DESC
LIMIT 10
"""
        elif "produkt" in query_lower:
            return "SELECT * FROM products ORDER BY price DESC LIMIT 10"
        elif "kunde" in query_lower or "customer" in query_lower:
            return "SELECT * FROM customers LIMIT 10"
        else:
            return "SELECT * FROM sales ORDER BY sale_date DESC LIMIT 10"

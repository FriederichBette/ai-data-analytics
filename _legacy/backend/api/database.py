"""
Database Manager für Supabase Integration
"""
from supabase import create_client, Client
from typing import List, Dict, Any, Optional
import os
from dotenv import load_dotenv

load_dotenv()


class DatabaseManager:
    """Manages database connections and queries to Supabase"""
    
    def __init__(self):
        self.supabase_url = os.getenv("SUPABASE_URL")
        self.supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_ANON_KEY")
        
        if not self.supabase_url or not self.supabase_key:
            raise ValueError("Supabase credentials not found in environment variables")
        
        self.client: Client = create_client(self.supabase_url, self.supabase_key)
    
    def is_connected(self) -> bool:
        """Check if database connection is active"""
        try:
            # Simple query to test connection
            self.client.table("sales").select("id").limit(1).execute()
            return True
        except:
            return False
    
    async def execute_query(self, sql_query: str, max_rows: int = 100) -> List[Dict[str, Any]]:
        """
        Execute a SQL query and return results
        
        Note: Supabase Python client uses PostgREST, not raw SQL.
        This is a simplified version. For production, use Supabase SQL functions.
        """
        try:
            # For now, we'll use the RPC method to execute raw SQL
            # You'll need to create a Postgres function in Supabase for this
            result = self.client.rpc('execute_sql', {'query': sql_query}).execute()
            return result.data[:max_rows] if result.data else []
        except Exception as e:
            raise Exception(f"Query execution failed: {str(e)}")
    
    async def get_schema_info(self) -> Dict[str, Any]:
        """Get information about database schema"""
        schema = {
            "tables": {
                "sales": {
                    "description": "Verkaufstransaktionen",
                    "columns": ["id", "product_id", "customer_id", "quantity", "total_amount", "sale_date", "created_at"]
                },
                "products": {
                    "description": "Produktkatalog",
                    "columns": ["id", "name", "category", "price", "cost", "margin", "created_at"]
                },
                "customers": {
                    "description": "Kundendaten",
                    "columns": ["id", "name", "email", "country", "city", "created_at"]
                }
            }
        }
        return schema
    
    async def list_tables(self) -> List[str]:
        """List all available tables"""
        return ["sales", "products", "customers"]
    
    async def get_table_data(self, table_name: str, limit: int = 100) -> List[Dict[str, Any]]:
        """Get data from a specific table"""
        try:
            result = self.client.table(table_name).select("*").limit(limit).execute()
            return result.data
        except Exception as e:
            raise Exception(f"Failed to fetch data from {table_name}: {str(e)}")

"""
Demo Data Generator - Generiert realistische Verkaufsdaten

Dieses Modul kann später durch echte API-Integrationen ersetzt werden.
"""
import random
from datetime import datetime, timedelta
from typing import List, Dict, Any
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()


class DataGenerator:
    """Generates realistic demo data for testing"""
    
    def __init__(self):
        self.supabase_url = os.getenv("SUPABASE_URL")
        self.supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_ANON_KEY")
        
        if self.supabase_url and self.supabase_key:
            self.client: Client = create_client(self.supabase_url, self.supabase_key)
        else:
            self.client = None
            print("⚠️  Supabase credentials not found")
    
    def generate_sales_data(self, num_records: int = 50) -> List[Dict[str, Any]]:
        """
        Generate random sales data
        
        Args:
            num_records: Number of sales records to generate
            
        Returns:
            List of sales dictionaries
        """
        sales = []
        
        for _ in range(num_records):
            # Random date in the last 365 days
            days_ago = random.randint(0, 365)
            sale_date = datetime.now() - timedelta(days=days_ago)
            
            sale = {
                "product_id": random.randint(1, 20),  # Assuming 20 products
                "customer_id": random.randint(1, 50),  # Assuming 50 customers
                "quantity": random.randint(1, 5),
                "total_amount": round(random.uniform(10, 2000), 2),
                "sale_date": sale_date.strftime("%Y-%m-%d"),
            }
            
            sales.append(sale)
        
        return sales
    
    def load_to_supabase(self, table_name: str, data: List[Dict[str, Any]]) -> bool:
        """
        Load data to Supabase
        
        Args:
            table_name: Name of the table
            data: List of records to insert
            
        Returns:
            True if successful, False otherwise
        """
        if not self.client:
            print("❌ Supabase client not initialized")
            return False
        
        try:
            result = self.client.table(table_name).insert(data).execute()
            print(f"✅ Loaded {len(data)} records to {table_name}")
            return True
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return False
    
    def run_etl_pipeline(self):
        """Run the complete ETL pipeline"""
        print("🚀 Starting ETL Pipeline...")
        
        # Generate data
        print("📊 Generating sales data...")
        sales_data = self.generate_sales_data(num_records=50)
        
        # Load to database
        print("💾 Loading to Supabase...")
        success = self.load_to_supabase("sales", sales_data)
        
        if success:
            print("✅ ETL Pipeline completed successfully!")
        else:
            print("❌ ETL Pipeline failed")
        
        return success


if __name__ == "__main__":
    # Test the data generator
    generator = DataGenerator()
    generator.run_etl_pipeline()

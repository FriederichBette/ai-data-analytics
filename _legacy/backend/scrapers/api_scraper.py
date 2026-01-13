"""
Example API Scraper - Holt Daten von öffentlichen APIs

Dieses Beispiel zeigt, wie man Daten von APIs holt und in Supabase lädt.
"""
import requests
from typing import List, Dict, Any, Optional
import os
from dotenv import load_dotenv

load_dotenv()


class APIDataScraper:
    """Scrapes data from public APIs"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Data-Analytics-LLM/1.0'
        })
    
    def fetch_crypto_prices(self, limit: int = 10) -> Optional[List[Dict[str, Any]]]:
        """
        Fetch cryptocurrency prices from CoinGecko API (free, no key needed)
        
        Args:
            limit: Number of coins to fetch
            
        Returns:
            List of crypto price data
        """
        try:
            url = "https://api.coingecko.com/api/v3/coins/markets"
            params = {
                "vs_currency": "eur",
                "order": "market_cap_desc",
                "per_page": limit,
                "page": 1,
                "sparkline": False
            }
            
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Transform data
            transformed = []
            for coin in data:
                transformed.append({
                    "name": coin["name"],
                    "symbol": coin["symbol"].upper(),
                    "price_eur": coin["current_price"],
                    "market_cap": coin["market_cap"],
                    "price_change_24h": coin["price_change_percentage_24h"],
                })
            
            print(f"✅ Fetched {len(transformed)} crypto prices")
            return transformed
            
        except Exception as e:
            print(f"❌ Error fetching crypto prices: {e}")
            return None
    
    def fetch_country_data(self) -> Optional[List[Dict[str, Any]]]:
        """
        Fetch country data from REST Countries API (free, no key needed)
        
        Returns:
            List of country data
        """
        try:
            url = "https://restcountries.com/v3.1/all"
            
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Transform data (nur wichtige Felder)
            transformed = []
            for country in data[:50]:  # Limit to 50 countries
                transformed.append({
                    "name": country.get("name", {}).get("common", "Unknown"),
                    "capital": country.get("capital", ["N/A"])[0] if country.get("capital") else "N/A",
                    "population": country.get("population", 0),
                    "region": country.get("region", "Unknown"),
                    "area": country.get("area", 0),
                })
            
            print(f"✅ Fetched {len(transformed)} countries")
            return transformed
            
        except Exception as e:
            print(f"❌ Error fetching country data: {e}")
            return None
    
    def run_scraping_pipeline(self):
        """Run the complete scraping pipeline"""
        print("🕷️  Starting Web Scraping Pipeline...")
        
        # Fetch crypto prices
        print("\n📈 Fetching cryptocurrency prices...")
        crypto_data = self.fetch_crypto_prices(limit=10)
        
        if crypto_data:
            print("\nTop 3 Cryptos:")
            for crypto in crypto_data[:3]:
                print(f"  {crypto['name']} ({crypto['symbol']}): €{crypto['price_eur']:,.2f}")
        
        # Fetch country data
        print("\n🌍 Fetching country data...")
        country_data = self.fetch_country_data()
        
        if country_data:
            print("\nTop 3 Countries by Population:")
            sorted_countries = sorted(country_data, key=lambda x: x['population'], reverse=True)
            for country in sorted_countries[:3]:
                print(f"  {country['name']}: {country['population']:,} people")
        
        print("\n✅ Scraping Pipeline completed!")
        
        return {
            "crypto": crypto_data,
            "countries": country_data
        }


if __name__ == "__main__":
    # Test the scraper
    scraper = APIDataScraper()
    results = scraper.run_scraping_pipeline()
    
    print(f"\n📊 Total data collected:")
    print(f"  - Cryptocurrencies: {len(results['crypto']) if results['crypto'] else 0}")
    print(f"  - Countries: {len(results['countries']) if results['countries'] else 0}")

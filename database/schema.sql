-- ============================================
-- Data Analytics LLM - Supabase Schema
-- ============================================

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ============================================
-- 1. PRODUCTS TABLE (Produktkatalog)
-- ============================================
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    cost DECIMAL(10, 2) NOT NULL CHECK (cost >= 0),
    margin DECIMAL(5, 2) GENERATED ALWAYS AS (
        CASE 
            WHEN price > 0 THEN ((price - cost) / price * 100)
            ELSE 0
        END
    ) STORED,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index for faster category searches
CREATE INDEX idx_products_category ON products(category);

-- ============================================
-- 2. CUSTOMERS TABLE (Kundendaten)
-- ============================================
CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    country VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index for faster country/city searches
CREATE INDEX idx_customers_country ON customers(country);
CREATE INDEX idx_customers_city ON customers(city);

-- ============================================
-- 3. SALES TABLE (Verkaufstransaktionen)
-- ============================================
CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    customer_id INTEGER NOT NULL REFERENCES customers(id) ON DELETE CASCADE,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    total_amount DECIMAL(10, 2) NOT NULL CHECK (total_amount >= 0),
    sale_date DATE NOT NULL DEFAULT CURRENT_DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes for faster queries
CREATE INDEX idx_sales_product_id ON sales(product_id);
CREATE INDEX idx_sales_customer_id ON sales(customer_id);
CREATE INDEX idx_sales_sale_date ON sales(sale_date);
CREATE INDEX idx_sales_total_amount ON sales(total_amount);

-- ============================================
-- 4. VIEWS (Für häufige Abfragen)
-- ============================================

-- Sales Summary View
CREATE OR REPLACE VIEW sales_summary AS
SELECT 
    s.id,
    s.sale_date,
    p.name AS product_name,
    p.category AS product_category,
    c.name AS customer_name,
    c.country AS customer_country,
    s.quantity,
    s.total_amount,
    p.price,
    p.cost,
    (s.total_amount - (p.cost * s.quantity)) AS profit
FROM sales s
JOIN products p ON s.product_id = p.id
JOIN customers c ON s.customer_id = c.id;

-- Monthly Sales View
CREATE OR REPLACE VIEW monthly_sales AS
SELECT 
    DATE_TRUNC('month', sale_date) AS month,
    COUNT(*) AS total_sales,
    SUM(quantity) AS total_quantity,
    SUM(total_amount) AS total_revenue
FROM sales
GROUP BY DATE_TRUNC('month', sale_date)
ORDER BY month DESC;

-- Top Products View
CREATE OR REPLACE VIEW top_products AS
SELECT 
    p.id,
    p.name,
    p.category,
    COUNT(s.id) AS sales_count,
    SUM(s.quantity) AS total_quantity_sold,
    SUM(s.total_amount) AS total_revenue
FROM products p
LEFT JOIN sales s ON p.id = s.product_id
GROUP BY p.id, p.name, p.category
ORDER BY total_revenue DESC;

-- ============================================
-- 5. FUNCTIONS (Für SQL Execution via API)
-- ============================================

-- Function to execute dynamic SQL (needed for LLM-generated queries)
-- WICHTIG: Diese Funktion sollte nur mit Service Role Key verwendet werden!
CREATE OR REPLACE FUNCTION execute_sql(query TEXT)
RETURNS JSON
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
DECLARE
    result JSON;
BEGIN
    -- Execute the query and return as JSON
    EXECUTE 'SELECT json_agg(t) FROM (' || query || ') t' INTO result;
    RETURN COALESCE(result, '[]'::JSON);
EXCEPTION
    WHEN OTHERS THEN
        RETURN json_build_object('error', SQLERRM);
END;
$$;

-- ============================================
-- 6. ROW LEVEL SECURITY (Optional)
-- ============================================

-- Enable RLS (kann später aktiviert werden)
-- ALTER TABLE products ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE customers ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE sales ENABLE ROW LEVEL SECURITY;

-- ============================================
-- FERTIG! Schema erstellt.
-- ============================================

-- Zeige alle Tabellen
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public' 
  AND table_type = 'BASE TABLE';

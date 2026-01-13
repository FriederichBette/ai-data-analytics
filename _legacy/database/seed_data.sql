-- ============================================
-- Demo Daten für Data Analytics LLM
-- ============================================

-- ============================================
-- 1. PRODUCTS (20 Produkte)
-- ============================================
INSERT INTO products (name, category, price, cost) VALUES
-- Electronics
('iPhone 15 Pro', 'Electronics', 1299.00, 800.00),
('Samsung Galaxy S24', 'Electronics', 999.00, 650.00),
('MacBook Pro 16"', 'Electronics', 2499.00, 1600.00),
('Dell XPS 15', 'Electronics', 1899.00, 1200.00),
('Sony WH-1000XM5', 'Electronics', 399.00, 200.00),
('AirPods Pro', 'Electronics', 279.00, 150.00),

-- Clothing
('Nike Air Max', 'Clothing', 159.00, 80.00),
('Adidas Ultraboost', 'Clothing', 189.00, 95.00),
('Levi''s 501 Jeans', 'Clothing', 89.00, 40.00),
('North Face Jacket', 'Clothing', 299.00, 150.00),
('H&M T-Shirt', 'Clothing', 19.00, 8.00),

-- Food & Beverage
('Organic Coffee Beans 1kg', 'Food', 24.99, 12.00),
('Premium Olive Oil', 'Food', 34.99, 18.00),
('Protein Powder 2kg', 'Food', 49.99, 25.00),
('Energy Drink 24-Pack', 'Food', 29.99, 15.00),

-- Home & Garden
('Dyson V15 Vacuum', 'Home', 699.00, 400.00),
('KitchenAid Mixer', 'Home', 449.00, 250.00),
('IKEA Desk', 'Home', 199.00, 100.00),
('Smart Thermostat', 'Home', 249.00, 130.00),
('LED Lamp', 'Home', 39.00, 18.00);

-- ============================================
-- 2. CUSTOMERS (50 Kunden)
-- ============================================
INSERT INTO customers (name, email, country, city) VALUES
-- Deutschland
('Max Mustermann', 'max.mustermann@email.de', 'Germany', 'Berlin'),
('Anna Schmidt', 'anna.schmidt@email.de', 'Germany', 'Munich'),
('Peter Weber', 'peter.weber@email.de', 'Germany', 'Hamburg'),
('Julia Fischer', 'julia.fischer@email.de', 'Germany', 'Frankfurt'),
('Michael Becker', 'michael.becker@email.de', 'Germany', 'Cologne'),
('Sarah Meyer', 'sarah.meyer@email.de', 'Germany', 'Stuttgart'),
('Thomas Wagner', 'thomas.wagner@email.de', 'Germany', 'Berlin'),
('Laura Hoffmann', 'laura.hoffmann@email.de', 'Germany', 'Munich'),
('Daniel Schulz', 'daniel.schulz@email.de', 'Germany', 'Hamburg'),
('Lisa Bauer', 'lisa.bauer@email.de', 'Germany', 'Frankfurt'),

-- Österreich
('Hans Gruber', 'hans.gruber@email.at', 'Austria', 'Vienna'),
('Maria Huber', 'maria.huber@email.at', 'Austria', 'Salzburg'),
('Franz Müller', 'franz.mueller@email.at', 'Austria', 'Graz'),
('Sophie Steiner', 'sophie.steiner@email.at', 'Austria', 'Vienna'),
('Wolfgang Berger', 'wolfgang.berger@email.at', 'Austria', 'Innsbruck'),

-- Schweiz
('Lukas Meier', 'lukas.meier@email.ch', 'Switzerland', 'Zurich'),
('Emma Keller', 'emma.keller@email.ch', 'Switzerland', 'Geneva'),
('Noah Schmid', 'noah.schmid@email.ch', 'Switzerland', 'Basel'),
('Mia Brunner', 'mia.brunner@email.ch', 'Switzerland', 'Zurich'),
('Leon Widmer', 'leon.widmer@email.ch', 'Switzerland', 'Bern'),

-- USA
('John Smith', 'john.smith@email.com', 'USA', 'New York'),
('Emily Johnson', 'emily.johnson@email.com', 'USA', 'Los Angeles'),
('Michael Brown', 'michael.brown@email.com', 'USA', 'Chicago'),
('Jessica Davis', 'jessica.davis@email.com', 'USA', 'Houston'),
('David Wilson', 'david.wilson@email.com', 'USA', 'San Francisco'),

-- UK
('James Taylor', 'james.taylor@email.co.uk', 'UK', 'London'),
('Olivia Anderson', 'olivia.anderson@email.co.uk', 'UK', 'Manchester'),
('William Thomas', 'william.thomas@email.co.uk', 'UK', 'Birmingham'),
('Sophie Martin', 'sophie.martin@email.co.uk', 'UK', 'London'),
('Harry White', 'harry.white@email.co.uk', 'UK', 'Edinburgh'),

-- Frankreich
('Pierre Dubois', 'pierre.dubois@email.fr', 'France', 'Paris'),
('Marie Laurent', 'marie.laurent@email.fr', 'France', 'Lyon'),
('Jean Bernard', 'jean.bernard@email.fr', 'France', 'Marseille'),
('Claire Petit', 'claire.petit@email.fr', 'France', 'Paris'),
('Antoine Roux', 'antoine.roux@email.fr', 'France', 'Nice'),

-- Spanien
('Carlos Garcia', 'carlos.garcia@email.es', 'Spain', 'Madrid'),
('Ana Martinez', 'ana.martinez@email.es', 'Spain', 'Barcelona'),
('Miguel Lopez', 'miguel.lopez@email.es', 'Spain', 'Valencia'),
('Isabel Rodriguez', 'isabel.rodriguez@email.es', 'Spain', 'Madrid'),
('Pablo Fernandez', 'pablo.fernandez@email.es', 'Spain', 'Seville'),

-- Italien
('Marco Rossi', 'marco.rossi@email.it', 'Italy', 'Rome'),
('Giulia Bianchi', 'giulia.bianchi@email.it', 'Italy', 'Milan'),
('Alessandro Ferrari', 'alessandro.ferrari@email.it', 'Italy', 'Florence'),
('Francesca Romano', 'francesca.romano@email.it', 'Italy', 'Rome'),
('Matteo Esposito', 'matteo.esposito@email.it', 'Italy', 'Naples'),

-- Niederlande
('Jan de Vries', 'jan.devries@email.nl', 'Netherlands', 'Amsterdam'),
('Eva van den Berg', 'eva.vandenberg@email.nl', 'Netherlands', 'Rotterdam'),
('Pieter Bakker', 'pieter.bakker@email.nl', 'Netherlands', 'Utrecht'),
('Lisa Janssen', 'lisa.janssen@email.nl', 'Netherlands', 'Amsterdam'),
('Tom Visser', 'tom.visser@email.nl', 'Netherlands', 'The Hague');

-- ============================================
-- 3. SALES (200 Verkäufe über 2024)
-- ============================================

-- Funktion zum Generieren von zufälligen Verkäufen
DO $$
DECLARE
    i INTEGER;
    random_product_id INTEGER;
    random_customer_id INTEGER;
    random_quantity INTEGER;
    product_price DECIMAL(10,2);
    random_date DATE;
BEGIN
    FOR i IN 1..200 LOOP
        -- Zufälliges Produkt
        random_product_id := (SELECT id FROM products ORDER BY RANDOM() LIMIT 1);
        
        -- Zufälliger Kunde
        random_customer_id := (SELECT id FROM customers ORDER BY RANDOM() LIMIT 1);
        
        -- Zufällige Menge (1-5)
        random_quantity := FLOOR(RANDOM() * 5 + 1)::INTEGER;
        
        -- Produktpreis holen
        SELECT price INTO product_price FROM products WHERE id = random_product_id;
        
        -- Zufälliges Datum in 2024
        random_date := DATE '2024-01-01' + (RANDOM() * 365)::INTEGER;
        
        -- Verkauf einfügen
        INSERT INTO sales (product_id, customer_id, quantity, total_amount, sale_date)
        VALUES (
            random_product_id,
            random_customer_id,
            random_quantity,
            product_price * random_quantity,
            random_date
        );
    END LOOP;
END $$;

-- ============================================
-- Fertig! Demo-Daten geladen.
-- ============================================

-- Zeige Statistiken
SELECT 
    'Products' AS table_name, 
    COUNT(*) AS count 
FROM products
UNION ALL
SELECT 
    'Customers' AS table_name, 
    COUNT(*) AS count 
FROM customers
UNION ALL
SELECT 
    'Sales' AS table_name, 
    COUNT(*) AS count 
FROM sales;

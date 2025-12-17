# 📊 Datenbank Setup

Dieses Verzeichnis enthält alle Datenbank-bezogenen Dateien für das Projekt.

## 🚀 Schema in Supabase importieren

### Schritt 1: Öffne den SQL Editor in Supabase

1. Gehe zu deinem Supabase Dashboard: https://supabase.com/dashboard/project/vauipkbigugewcqgnowk
2. Klicke auf **SQL Editor** in der linken Sidebar
3. Klicke auf **New Query**

### Schritt 2: Schema importieren

1. Öffne die Datei `schema.sql` in diesem Verzeichnis
2. Kopiere den gesamten Inhalt
3. Füge ihn in den SQL Editor ein
4. Klicke auf **Run** (oder drücke Ctrl+Enter)

Das Schema erstellt:
- ✅ 3 Tabellen: `products`, `customers`, `sales`
- ✅ Indexes für schnelle Abfragen
- ✅ Views für häufige Analysen
- ✅ SQL Execution Function für LLM-Queries

### Schritt 3: Demo-Daten laden (optional)

1. Öffne die Datei `seed_data.sql`
2. Kopiere den Inhalt
3. Füge ihn in einen neuen SQL Query ein
4. Klicke auf **Run**

Dies lädt:
- 20 Produkte
- 50 Kunden
- 200 Verkaufstransaktionen

## 📋 Tabellen-Übersicht

### products (Produkte)
- `id`: Eindeutige ID
- `name`: Produktname
- `category`: Kategorie (Electronics, Clothing, Food, etc.)
- `price`: Verkaufspreis
- `cost`: Einkaufspreis
- `margin`: Gewinnmarge (automatisch berechnet)

### customers (Kunden)
- `id`: Eindeutige ID
- `name`: Kundenname
- `email`: E-Mail Adresse
- `country`: Land
- `city`: Stadt

### sales (Verkäufe)
- `id`: Eindeutige ID
- `product_id`: Referenz zu Produkt
- `customer_id`: Referenz zu Kunde
- `quantity`: Anzahl verkaufter Einheiten
- `total_amount`: Gesamtumsatz
- `sale_date`: Verkaufsdatum

## 🔍 Nützliche Views

- `sales_summary`: Vollständige Verkaufsübersicht mit Joins
- `monthly_sales`: Monatliche Verkaufsstatistiken
- `top_products`: Bestseller-Produkte

## ⚠️ Wichtig

Die `execute_sql()` Funktion erlaubt dynamische SQL-Ausführung. Stelle sicher, dass:
- Du den **Service Role Key** verwendest (nicht den anon key)
- Die Funktion nur vom Backend aufgerufen wird
- User-Input validiert wird, um SQL-Injection zu vermeiden

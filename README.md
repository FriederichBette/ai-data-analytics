# 🚀 Data Analytics LLM - Natürlichsprachliche Datenbank-Abfragen

Ein vollständiges System für automatische Datenintegration, Standardisierung und LLM-basierte SQL-Abfragen.

## 📋 Features

- **Automatische Datenintegration**: Web Scraping & API-Integration
- **ETL Pipeline**: Datenstandardisierung und -validierung
- **Data Marts**: Strukturierte Datenspeicherung in Supabase
- **LLM Text-to-SQL**: Natürlichsprachliche Abfragen (OpenAI oder Ollama)
- **Interaktives UI**: Dashboard für Datenabfragen und Visualisierung
- **Hybride Speicherung**: Strukturierte Daten + Vektoren (optional)

## 🏗️ Architektur

```
┌─────────────┐
│   Frontend  │  Next.js Dashboard
│   (Next.js) │  Natürlichsprachliche Eingabe
└──────┬──────┘
       │
┌──────▼──────┐
│   Backend   │  Python FastAPI
│   (Python)  │  - LLM Integration (OpenAI/Ollama)
│             │  - ETL Pipeline
│             │  - Data Validation
└──────┬──────┘
       │
┌──────▼──────┐
│  Supabase   │  PostgreSQL Database
│  (Postgres) │  - Data Marts (Sales, Products, etc.)
│             │  - pgvector (optional)
└─────────────┘
```

## 🚀 Quick Start

### 1. Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 2. Umgebungsvariablen konfigurieren

Kopiere `.env.example` zu `.env` und fülle die Werte aus:

```bash
cp .env.example .env
```

### 3. Datenbank initialisieren

```bash
cd database
# Schema in Supabase importieren (siehe database/README.md)
```

### 4. Backend starten

```bash
cd backend
python main.py
```

### 5. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Öffne http://localhost:3000

## 📁 Projektstruktur

```
data-analytics-llm/
├── backend/
│   ├── etl/              # ETL Pipelines
│   ├── scrapers/         # Web Scraping Module
│   ├── llm/              # LLM Text-to-SQL
│   ├── api/              # FastAPI Endpoints
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── app/          # Next.js App Router
│   │   ├── components/   # React Components
│   │   └── lib/          # Utilities
│   └── package.json
├── database/
│   ├── schema.sql        # Supabase Schema
│   ├── migrations/       # DB Migrations
│   └── seed_data.sql     # Demo Daten
├── .env.example
├── .gitignore
└── README.md
```

## 🔑 Konfiguration

### LLM Provider wählen

In `.env`:

**OpenAI (Cloud)**:
```
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-...
```

**Ollama (Lokal)**:
```
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama3
OLLAMA_BASE_URL=http://localhost:11434
```

## 📊 Beispiel-Abfragen

- "Zeige mir die Top 10 Verkäufe im August sortiert nach Umsatz"
- "Welche Produkte haben die höchste Marge?"
- "Wie viele Kunden haben wir in Deutschland?"
- "Vergleiche Umsatz Q1 vs Q2 2024"

## 🛠️ Technologie-Stack

- **Backend**: Python, FastAPI, SQLAlchemy
- **Frontend**: Next.js 14, React, TypeScript, Tailwind CSS
- **Database**: Supabase (PostgreSQL + pgvector)
- **LLM**: OpenAI GPT-4 oder Ollama (Llama 3)
- **ETL**: Pandas, BeautifulSoup, Requests

## 📝 Lizenz

MIT

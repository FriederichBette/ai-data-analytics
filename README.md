# Local Data Analytics Platform

A privacy-focused data analytics tool that allows users to query a PostgreSQL database using natural language. The system runs locally, leveraging an LLM (Gemma 2 via Ollama) to translate questions into SQL queries.

## Architecture

This project follows a three-tier architecture:
- **Frontend:** Next.js (React/TypeScript) styled with Tailwind CSS. Provides a clean, Google-inspired interface.
- **Backend:** Python FastAPI. Handles request processing, prompt engineering, and database execution.
- **Database:** PostgreSQL (Supabase).
- **Inference:** Local LLM via Ollama (`gemma2:2b`).

## Prerequisites

1.  **Ollama**: Must be installed and running locally.
    -   Model: `ollama pull gemma2:2b`
2.  **Supabase Account**: A PostgreSQL database (free tier sufficient).
3.  **Python 3.10+** and **Node.js 18+**.

## Installation

### 1. Clone Repository
```bash
git clone <repository-url>
cd data-analytics-llm
```

### 2. Backend Setup
```bash
cd backend
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
```

**Configuration:**
Create a `.env` file in the `backend/` directory:
```env
DATABASE_URL=postgresql://postgres:[PASSWORD]@db.[PROJECT-ID].supabase.co:5432/postgres
OLLAMA_URL=http://127.0.0.1:11434/api/generate
OLLAMA_MODEL=gemma2:2b
```

### 3. Frontend Setup
```bash
cd frontend
npm install
```

## Running the Application

1.  Start Ollama (ensure it is running in the background).
2.  Start Backend (Port 8080):
    ```bash
    cd backend
    .\venv\Scripts\Activate
    uvicorn main:app --reload --port 8080
    ```
3.  Start Frontend (Port 3000):
    ```bash
    cd frontend
    npm run dev
    ```
4.  Open browser at `http://localhost:3000`.

---

## Usage Guide (Prompts)

The system uses a small local model (`gemma2:2b`). For best results, use precise and simple language. The database contains a `transactions` table with columns: `date`, `category`, `amount`, `description`. 

**Note on Financial Data:** Expenses are stored as negative values (e.g., -50.00), Income as positive values.

### Query Examples

**1. Viewing Data**
*   "Show all transactions."
*   "Show the last 5 transactions."
*   "Show all transactions from January 2024."

**2. Aggregations (Sums)**
*   "What is the total sum of all expenses?"
    *   *Result:* Calculates sum of all negative values.
*   "How much did I spend on 'Lebensmittel'?"
    *   *Result:* Sums amount where category is 'Lebensmittel'.
*   "What is my total income?"
    *   *Result:* Sums all positive values (e.g., salary).

**3. Filtering**
*   "Show all expenses greater than 100 Euro."
    *   *Note:* The LLM understands "expenses", but technically asks for `amount < -100`.
*   "List all transactions for the category 'Miete'."

**4. Complex Queries**
*   "What was the most expensive transaction?"
    *   *Prompt:* "Sort by amount ascending limit 1".

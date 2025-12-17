# LLM Data Analytics Platform

## Project Overview
This project provides a local data analytics platform that allows users to query a database using natural language. It leverages a local Large Language Model (LLM) via Ollama to translate natural language questions into executable SQL queries. The system is designed for privacy, performance, and ease of deployment.

## Key Features
*   **Natural Language Interface**: Users can ask questions in plain German or English (e.g., "How many customers do we have?").
*   **Local Processing**: Uses Gemma 2 (2B) via Ollama for privacy-preserving, offline inference.
*   **Modern Stack**: Built with Python (FastAPI) for the backend and Next.js (TypeScript) for the frontend.
*   **Database Integration**: Connects to a Supabase (PostgreSQL) database.
*   **Automated setup**: Includes batch scripts for one-click installation and startup on Windows.

## Technology Stack

### Backend
*   **Framework**: FastAPI (Python)
*   **LLM Integration**: Custom Text-to-SQL Engine supporting Ollama and OpenAI.
*   **Database**: Supabase (PostgreSQL) via `supabase-py`.

### Frontend
*   **Framework**: Next.js 14 (App Router)
*   **Language**: TypeScript
*   **Styling**: Tailwind CSS with custom glassmorphism design.

## Prerequisites
*   **Windows OS** (Project is optimized for Windows environments)
*   **Ollama**: Must be installed and running.
*   **Python**: Version 3.10 or higher.
*   **Node.js**: Version 18 or higher.

## Installation and Setup

### 1. Database Setup
The project requires a Supabase database.
1.  Navigate to the `database/` directory.
2.  Execute `schema.sql` in your Supabase SQL Editor to create tables.
3.  Execute `seed_data.sql` to populate the database with demo data.

### 2. Environment Configuration
The application requires specific environment variables. A start script handles this automatically, but you can configure it manually in a `.env` file (see `.env.example`).

### 3. Automatic Startup (Recommended)
Double-click the `FINAL_START.bat` file in the root directory. This script will:
1.  Check for dependencies.
2.  Set up the Python virtual environment.
3.  Install all backend and frontend packages.
4.  Start the Ollama LLM service (if not running).
5.  Launch both the Backend API and Frontend UI.

## Architecture

### Text-to-SQL Engine
The core logic resides in `backend/llm/text_to_sql.py`. It constructs a prompt containing the database schema and the user's query, sends it to the LLM, and sanitizes the returned SQL.

### Security Note
The current implementation is designed for read-only analytics. In a production environment, ensure the database user has restricted permissions (READ ONLY) to prevent SQL injection attacks modifying data.

## License
MIT License

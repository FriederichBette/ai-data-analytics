@echo off
chcp 65001 > nul
echo ===================================================
echo 🚀 Data Analytics Platform - Start Script
echo ===================================================
echo.

:: Check for .env file
if not exist .env (
    echo ❌ ERROR: .env file not found!
    echo.
    echo Please copy '.env.example' to '.env' and fill in your credentials.
    echo.
    pause
    exit
)

echo 1. Checking Backend Setup...
cd backend
if not exist venv (
    echo 📦 Creating Python virtual environment...
    python -m venv venv
)
echo 📥 Installing/Updating Python dependencies...
venv\Scripts\pip install -q -r requirements.txt

echo 2. Checking Frontend Setup...
cd ..\frontend
if not exist node_modules (
    echo 📥 Installing Node modules...
    call npm install --silent
)

echo.
echo 3. Starting Services...
cd ..
start "Backend API" cmd /k "cd backend && venv\Scripts\python main.py"
start "Frontend UI" cmd /k "cd frontend && npm run dev"

echo.
echo ✅ Services started! 
echo Open http://localhost:3000
echo.
pause

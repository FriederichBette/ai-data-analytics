# ============================================
# Data Analytics LLM - Automatisches Setup
# ============================================

Write-Host "🚀 Starting Data Analytics LLM Setup..." -ForegroundColor Cyan
Write-Host ""

# Prüfe ob wir im richtigen Verzeichnis sind
if (-not (Test-Path "backend\main.py")) {
    Write-Host "❌ Fehler: Bitte führe dieses Script im Projekt-Root aus!" -ForegroundColor Red
    exit 1
}

# ============================================
# 1. .env Datei erstellen
# ============================================
Write-Host "📝 Erstelle .env Datei..." -ForegroundColor Yellow

$envContent = @"
# Supabase Configuration
SUPABASE_URL=https://vauipkbigugewcqgnowk.supabase.co
SUPABASE_ANON_KEY=sb_publishable_m1BICcWcwdpMBw9J7GO19g_LA8rlw0q
SUPABASE_SERVICE_ROLE_KEY=sb_secret_xdWQQGWS5wXCvhbO4fFvzg_aQoN64rG

# LLM Provider (openai or ollama)
LLM_PROVIDER=ollama

# OpenAI Configuration (wenn du OpenAI nutzen möchtest)
# OPENAI_API_KEY=sk-your-openai-key-here
OPENAI_MODEL=gpt-4o-mini

# Ollama Configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=gemma2:2b

# Backend Configuration
BACKEND_PORT=8000
BACKEND_HOST=0.0.0.0

# Frontend Configuration
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_SUPABASE_URL=https://vauipkbigugewcqgnowk.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=sb_publishable_m1BICcWcwdpMBw9J7GO19g_LA8rlw0q
"@

Set-Content -Path ".env" -Value $envContent
Write-Host "✅ .env Datei erstellt!" -ForegroundColor Green
Write-Host ""

# ============================================
# 2. Backend Setup
# ============================================
Write-Host "🐍 Backend Setup..." -ForegroundColor Yellow

cd backend

# Virtual Environment erstellen
if (-not (Test-Path "venv")) {
    Write-Host "  📦 Erstelle Virtual Environment..." -ForegroundColor Cyan
    python -m venv venv
}

# Virtual Environment aktivieren
Write-Host "  🔧 Aktiviere Virtual Environment..." -ForegroundColor Cyan
& ".\venv\Scripts\Activate.ps1"

# Dependencies installieren
Write-Host "  📥 Installiere Python Dependencies..." -ForegroundColor Cyan
pip install -q -r requirements.txt

Write-Host "✅ Backend Setup abgeschlossen!" -ForegroundColor Green
Write-Host ""

cd ..

# ============================================
# 3. Frontend Setup
# ============================================
Write-Host "🎨 Frontend Setup..." -ForegroundColor Yellow

cd frontend

Write-Host "  📥 Installiere Node Dependencies..." -ForegroundColor Cyan
npm install --silent

Write-Host "✅ Frontend Setup abgeschlossen!" -ForegroundColor Green
Write-Host ""

cd ..

# ============================================
# 4. Fertig!
# ============================================
Write-Host "🎉 Setup abgeschlossen!" -ForegroundColor Green
Write-Host ""
Write-Host "📋 Nächste Schritte:" -ForegroundColor Cyan
Write-Host ""
Write-Host "1️⃣  Datenbank einrichten:" -ForegroundColor Yellow
Write-Host "   - Öffne: https://supabase.com/dashboard/project/vauipkbigugewcqgnowk/sql/new"
Write-Host "   - Führe 'database\schema.sql' aus"
Write-Host "   - Führe 'database\seed_data.sql' aus"
Write-Host ""
Write-Host "2️⃣  Backend starten:" -ForegroundColor Yellow
Write-Host "   cd backend"
Write-Host "   .\venv\Scripts\Activate.ps1"
Write-Host "   python main.py"
Write-Host ""
Write-Host "3️⃣  Frontend starten (neues Terminal):" -ForegroundColor Yellow
Write-Host "   cd frontend"
Write-Host "   npm run dev"
Write-Host ""
Write-Host "4️⃣  Öffne http://localhost:3000 im Browser!" -ForegroundColor Yellow
Write-Host ""
Write-Host "💡 Tipp: Stelle sicher, dass Ollama läuft: ollama serve" -ForegroundColor Cyan
Write-Host ""

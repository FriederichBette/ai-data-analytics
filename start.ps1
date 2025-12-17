# ============================================
# Data Analytics LLM - Start Script
# ============================================

Write-Host "🚀 Starting Data Analytics LLM..." -ForegroundColor Cyan
Write-Host ""

# Prüfe ob Setup durchgeführt wurde
if (-not (Test-Path ".env")) {
    Write-Host "❌ .env Datei nicht gefunden!" -ForegroundColor Red
    Write-Host "💡 Bitte führe zuerst 'setup.ps1' aus" -ForegroundColor Yellow
    exit 1
}

# Prüfe ob Backend venv existiert
if (-not (Test-Path "backend\venv")) {
    Write-Host "❌ Backend Virtual Environment nicht gefunden!" -ForegroundColor Red
    Write-Host "💡 Bitte führe zuerst 'setup.ps1' aus" -ForegroundColor Yellow
    exit 1
}

# Prüfe ob Frontend node_modules existiert
if (-not (Test-Path "frontend\node_modules")) {
    Write-Host "❌ Frontend Dependencies nicht gefunden!" -ForegroundColor Red
    Write-Host "💡 Bitte führe zuerst 'setup.ps1' aus" -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Alle Voraussetzungen erfüllt!" -ForegroundColor Green
Write-Host ""

# ============================================
# Backend starten
# ============================================
Write-Host "🐍 Starte Backend..." -ForegroundColor Yellow

$backendJob = Start-Job -ScriptBlock {
    Set-Location $using:PWD
    cd backend
    & ".\venv\Scripts\python.exe" main.py
}

Start-Sleep -Seconds 3

# ============================================
# Frontend starten
# ============================================
Write-Host "🎨 Starte Frontend..." -ForegroundColor Yellow

$frontendJob = Start-Job -ScriptBlock {
    Set-Location $using:PWD
    cd frontend
    npm run dev
}

Start-Sleep -Seconds 5

# ============================================
# Status anzeigen
# ============================================
Write-Host ""
Write-Host "🎉 Alles läuft!" -ForegroundColor Green
Write-Host ""
Write-Host "📊 Services:" -ForegroundColor Cyan
Write-Host "  Backend:  http://localhost:8000" -ForegroundColor White
Write-Host "  Frontend: http://localhost:3000" -ForegroundColor White
Write-Host ""
Write-Host "💡 Öffne http://localhost:3000 im Browser!" -ForegroundColor Yellow
Write-Host ""
Write-Host "⏹️  Zum Beenden: Drücke Ctrl+C" -ForegroundColor Red
Write-Host ""

# Warte auf Benutzer-Abbruch
try {
    while ($true) {
        Start-Sleep -Seconds 1
    }
} finally {
    Write-Host ""
    Write-Host "🛑 Stoppe Services..." -ForegroundColor Yellow
    Stop-Job $backendJob
    Stop-Job $frontendJob
    Remove-Job $backendJob
    Remove-Job $frontendJob
    Write-Host "✅ Alle Services gestoppt!" -ForegroundColor Green
}

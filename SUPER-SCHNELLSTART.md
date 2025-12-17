# 🚀 SUPER SCHNELLSTART - 3 Befehle!

## 📍 Schritt 1: Projekt auf Desktop kopieren

Öffne PowerShell und führe aus:

```powershell
Copy-Item -Path "C:\Users\user\.gemini\antigravity\scratch\data-analytics-llm" -Destination "C:\Users\user\Desktop\data-analytics-llm" -Recurse
cd C:\Users\user\Desktop\data-analytics-llm
```

---

## 🔧 Schritt 2: Automatisches Setup

```powershell
.\setup.ps1
```

Das Script:
- ✅ Erstellt `.env` Datei mit deinen Credentials
- ✅ Installiert Python Dependencies
- ✅ Installiert Node Dependencies

**Dauer: ~2-3 Minuten**

---

## 🗄️ Schritt 3: Datenbank einrichten (einmalig)

1. Öffne: https://supabase.com/dashboard/project/vauipkbigugewcqgnowk/sql/new

2. **Schema importieren:**
   - Öffne `database\schema.sql` in einem Editor
   - Kopiere den gesamten Inhalt
   - Füge ihn im Supabase SQL Editor ein
   - Klicke **Run**

3. **Demo-Daten laden:**
   - Öffne `database\seed_data.sql`
   - Kopiere den Inhalt
   - Füge ihn im SQL Editor ein
   - Klicke **Run**

✅ **Fertig!** Du hast jetzt 20 Produkte, 50 Kunden, 200 Verkäufe

---

## 🚀 Schritt 4: Alles starten

```powershell
.\start.ps1
```

Das Script startet automatisch:
- 🐍 Backend (http://localhost:8000)
- 🎨 Frontend (http://localhost:3000)

**Öffne dann:** http://localhost:3000

---

## 🎉 FERTIG!

Stelle jetzt deine erste Frage:
- "Zeige mir alle Produkte"
- "Welche Kunden haben wir in Deutschland?"
- "Top 10 Verkäufe sortiert nach Umsatz"

---

## 💡 Wichtig: Ollama

Stelle sicher, dass Ollama läuft:

```powershell
ollama serve
```

Prüfe ob Gemma 2 verfügbar ist:

```powershell
ollama list
```

---

## 🛑 Stoppen

Drücke `Ctrl+C` im Terminal wo `start.ps1` läuft.

---

## 📁 Projekt-Struktur

```
C:\Users\user\Desktop\data-analytics-llm\
├── setup.ps1          ← Einmalig ausführen
├── start.ps1          ← Zum Starten
├── backend/           ← Python Backend
├── frontend/          ← Next.js Frontend
└── database/          ← SQL Dateien
```

---

## 🆘 Probleme?

### Setup.ps1 funktioniert nicht?
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\setup.ps1
```

### Backend startet nicht?
- Prüfe ob Python installiert ist: `python --version`
- Prüfe ob Supabase Credentials korrekt sind

### Frontend startet nicht?
- Prüfe ob Node.js installiert ist: `node --version`

---

## 🎯 Das war's!

**3 Befehle und du bist fertig:**

1. `Copy-Item ...` (Projekt kopieren)
2. `.\setup.ps1` (Setup)
3. `.\start.ps1` (Starten)

**Viel Spaß! 🚀**

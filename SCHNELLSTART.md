# 🚀 Schnellstart-Anleitung

## ✅ Phase 1 - ABGESCHLOSSEN!

Dein Projekt ist jetzt vollständig eingerichtet! Hier sind die nächsten Schritte:

## 📍 Projektstandort

```
C:\Users\user\.gemini\antigravity\scratch\data-analytics-llm\
```

**WICHTIG**: Öffne diesen Ordner als Workspace in deinem Editor!

---

## 🔧 Schritt 1: Datenbank einrichten (5 Minuten)

### 1.1 Schema importieren

1. Öffne dein Supabase Dashboard: https://supabase.com/dashboard/project/vauipkbigugewcqgnowk
2. Klicke auf **SQL Editor** (linke Sidebar)
3. Klicke auf **New Query**
4. Öffne die Datei `database/schema.sql` in diesem Projekt
5. Kopiere den gesamten Inhalt und füge ihn im SQL Editor ein
6. Klicke auf **Run** (oder Ctrl+Enter)

✅ Du solltest sehen: "Tables created successfully"

### 1.2 Demo-Daten laden

1. Im SQL Editor, klicke auf **New Query**
2. Öffne die Datei `database/seed_data.sql`
3. Kopiere den Inhalt und füge ihn ein
4. Klicke auf **Run**

✅ Du solltest sehen: 20 Products, 50 Customers, 200 Sales

---

## 🐍 Schritt 2: Backend starten (2 Minuten)

### 2.1 Python Virtual Environment erstellen

```powershell
cd C:\Users\user\.gemini\antigravity\scratch\data-analytics-llm\backend
python -m venv venv
.\venv\Scripts\activate
```

### 2.2 Dependencies installieren

```powershell
pip install -r requirements.txt
```

### 2.3 Backend starten

```powershell
python main.py
```

✅ Backend läuft auf: http://localhost:8000

**Teste es**: Öffne http://localhost:8000 im Browser - du solltest sehen:
```json
{
  "status": "online",
  "service": "Data Analytics LLM API"
}
```

---

## 🎨 Schritt 3: Frontend starten (2 Minuten)

### 3.1 Dependencies installieren

Öffne ein **NEUES Terminal** (lass das Backend laufen!):

```powershell
cd C:\Users\user\.gemini\antigravity\scratch\data-analytics-llm\frontend
npm install
```

### 3.2 Frontend starten

```powershell
npm run dev
```

✅ Frontend läuft auf: http://localhost:3000

---

## 🎉 Schritt 4: Erste Abfrage testen!

1. Öffne http://localhost:3000 im Browser
2. Du siehst ein schönes Dashboard mit Gradient-Hintergrund
3. Gib eine Frage ein, z.B.:
   - "Zeige mir alle Produkte"
   - "Welche Kunden haben wir in Deutschland?"
   - "Top 10 Verkäufe sortiert nach Umsatz"
4. Klicke auf **Abfrage starten**

**Hinweis**: Ohne OpenAI/Ollama werden Demo-Queries verwendet. Das System funktioniert trotzdem!

---

## 🤖 Optional: LLM konfigurieren

### Option A: Ollama (Kostenlos, Lokal)

Wenn du Ollama bereits installiert hast:

```powershell
# Starte Ollama
ollama serve

# In einem neuen Terminal:
ollama pull llama3
```

Die `.env` Datei ist bereits auf Ollama konfiguriert!

### Option B: OpenAI (Bezahlt, Cloud)

1. Erstelle einen API Key: https://platform.openai.com/api-keys
2. Öffne die Datei `.env` im Projekt-Root
3. Ändere:
   ```
   LLM_PROVIDER=openai
   OPENAI_API_KEY=sk-dein-key-hier
   ```
4. Starte das Backend neu

---

## 📊 Beispiel-Abfragen zum Testen

- "Zeige mir die Top 10 Verkäufe im August sortiert nach Umsatz"
- "Welche Produkte haben die höchste Marge?"
- "Wie viele Kunden haben wir in Deutschland?"
- "Liste alle Electronics Produkte"
- "Zeige mir alle Verkäufe von heute"

---

## 🐛 Troubleshooting

### Backend startet nicht?
- Prüfe ob Python installiert ist: `python --version`
- Prüfe ob venv aktiviert ist (du solltest `(venv)` im Terminal sehen)
- Prüfe die Supabase Credentials in `.env`

### Frontend startet nicht?
- Prüfe ob Node.js installiert ist: `node --version`
- Lösche `node_modules` und führe `npm install` erneut aus

### Keine Daten in der Datenbank?
- Hast du `schema.sql` und `seed_data.sql` ausgeführt?
- Prüfe im Supabase Dashboard unter "Table Editor"

### LLM funktioniert nicht?
- Das ist OK! Das System nutzt Demo-Queries als Fallback
- Für echte Text-to-SQL: Installiere Ollama oder füge OpenAI Key hinzu

---

## 📁 Projektstruktur

```
data-analytics-llm/
├── backend/           # Python FastAPI Backend
│   ├── api/          # Database Manager
│   ├── llm/          # Text-to-SQL Engine
│   └── main.py       # Hauptdatei
├── frontend/         # Next.js Frontend
│   ├── app/          # Pages
│   └── components/   # React Components
├── database/         # SQL Schema & Seed Data
└── .env             # Konfiguration (nicht in Git!)
```

---

## 🎯 Nächste Schritte (Phase 2+)

- [ ] ETL Pipeline für echte Datenquellen
- [ ] Web Scraping Module
- [ ] Erweiterte Visualisierungen
- [ ] Vektorsuche mit pgvector
- [ ] Query-Historie speichern
- [ ] Export-Funktionen (CSV, Excel)

---

## 💡 Tipps

- **Git**: Dein Projekt ist bereits ein Git Repository!
  ```powershell
  git status
  git log
  ```

- **Workspace**: Öffne den Ordner als Workspace:
  ```
  C:\Users\user\.gemini\antigravity\scratch\data-analytics-llm
  ```

- **Dokumentation**: Alle Details findest du in `README.md`

---

## 🆘 Hilfe benötigt?

Frag mich einfach! Ich kann dir helfen mit:
- Debugging
- Neue Features hinzufügen
- Datenquellen integrieren
- Performance-Optimierung

**Viel Erfolg! 🚀**

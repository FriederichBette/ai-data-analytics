"use client";

import { useState } from "react";
import { Search, Send, Database, Terminal, Activity, AlertCircle, ArrowRight } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

export default function Home() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<any>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  const handleQuery = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;

    setIsLoading(true);
    setResults(null);
    setError("");

    try {
      // WICHTIG: Port Wechsel auf 8080
      const res = await fetch("http://127.0.0.1:8080/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ natural_language_query: query }),
      });

      const data = await res.json();

      if (!res.ok) throw new Error(data.detail || "Verbindungsfehler");
      if (data.error) throw new Error(data.error);

      setResults(data);
    } catch (err: any) {
      console.error(err);
      setError("Verbindung zum Backend fehlgeschlagen. (Ist der Supabase Key in der .env gesetzt?)");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#131314] text-[#E3E3E3] font-sans flex flex-col items-center pt-[15vh]">

      <main className="w-full max-w-3xl px-6 flex flex-col gap-8">

        {/* Minimal Header */}
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center space-y-2 mb-4"
        >
          <h1 className="text-4xl font-medium tracking-tight text-white">
            Data Analytics
          </h1>
          <p className="text-[#A8C7FA] text-lg font-normal">
            Was möchtest du wissen?
          </p>
        </motion.div>

        {/* Google-like Search Bar */}
        <div className="relative w-full group">
          <form onSubmit={handleQuery} className="relative flex items-center bg-[#303134] rounded-[24px] shadow-lg transition-all hover:bg-[#3c4043] hover:shadow-xl focus-within:bg-[#3c4043] focus-within:shadow-xl">
            {/* Search Icon */}
            <div className="pl-6 pr-4 text-[#9AA0A6]">
              <Search size={24} />
            </div>

            {/* High Contrast Input */}
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Frage stellen..."
              className="w-full bg-transparent border-none text-white text-[18px] placeholder-[#9AA0A6] focus:outline-none h-[64px] font-normal"
              autoFocus
            />

            {/* Action Button */}
            <div className="pr-4">
              <button
                type="submit"
                disabled={isLoading}
                className="p-3 text-[#A8C7FA] hover:bg-[#444746] rounded-full transition-colors disabled:opacity-50"
              >
                {isLoading ? <Activity className="animate-spin" size={24} /> : <ArrowRight size={24} />}
              </button>
            </div>
          </form>
        </div>

        {/* Results Area - Clean Cards */}
        <div className="w-full mt-6">
          <AnimatePresence mode="wait">

            {error && (
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                className="p-4 rounded-xl bg-[#3C1917] border border-[#F2B8B5] text-[#F2B8B5] flex items-center gap-3"
              >
                <AlertCircle size={20} />
                <span className="font-medium">{error}</span>
              </motion.div>
            )}

            {results && (
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="space-y-6"
              >
                {/* SQL Code Snippet - Discreet */}
                <div className="pl-4 border-l-2 border-[#444746]">
                  <div className="text-xs font-medium text-[#9AA0A6] mb-1 uppercase tracking-wider">Generiertes SQL</div>
                  <code className="text-sm font-mono text-[#E3E3E3] break-all">
                    {results.sql_query}
                  </code>
                </div>

                {/* Main Data Card */}
                <div className="bg-[#1E1F20] rounded-2xl overflow-hidden border border-[#444746] shadow-sm">

                  <div className="p-6 border-b border-[#444746] flex items-center justify-between">
                    <h3 className="text-lg font-medium text-white flex items-center gap-2">
                      Ergebnis
                    </h3>
                    <span className="text-xs text-[#9AA0A6] bg-[#303134] px-2 py-1 rounded-md">
                      {results.data ? results.data.length : 0} Zeilen
                    </span>
                  </div>

                  <div className="overflow-x-auto">
                    {results.data && results.data.length > 0 ? (
                      <table className="w-full text-left border-collapse">
                        <thead className="bg-[#303134]">
                          <tr>
                            {Object.keys(results.data[0]).map((key) => (
                              <th key={key} className="px-6 py-4 text-xs font-medium text-[#E3E3E3] uppercase tracking-wider whitespace-nowrap">
                                {key}
                              </th>
                            ))}
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-[#444746]">
                          {results.data.map((row: any, i: number) => (
                            <tr key={i} className="hover:bg-[#303134] transition-colors">
                              {Object.values(row).map((val: any, j: number) => (
                                <td key={j} className="px-6 py-4 text-sm text-[#C4C7C5] whitespace-nowrap">
                                  {val !== null ? String(val) : <span className="opacity-20">-</span>}
                                </td>
                              ))}
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    ) : (
                      <div className="p-12 text-center text-[#9AA0A6]">
                        Keine Daten gefunden für diese Anfrage.
                      </div>
                    )}
                  </div>
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      </main>
    </div>
  );
}

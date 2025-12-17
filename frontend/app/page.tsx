"use client";

import { useState } from "react";
import QueryInterface from "@/components/QueryInterface";
import ResultsDisplay from "@/components/ResultsDisplay";
import Header from "@/components/Header";

export default function Home() {
  const [results, setResults] = useState<any>(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleQuery = async (query: string) => {
    setIsLoading(true);
    setResults(null);

    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/query`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ query }),
      });

      const data = await response.json();
      setResults(data);
    } catch (error) {
      setResults({
        success: false,
        error: "Verbindung zum Backend fehlgeschlagen. Stelle sicher, dass das Backend läuft.",
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      <div className="absolute inset-0 bg-[url('/grid.svg')] bg-center [mask-image:linear-gradient(180deg,white,rgba(255,255,255,0))]"></div>

      <div className="relative">
        <Header />

        <main className="container mx-auto px-4 py-12 max-w-6xl">
          <div className="text-center mb-12">
            <h1 className="text-5xl font-bold text-white mb-4 bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
              Data Analytics LLM
            </h1>
            <p className="text-xl text-gray-300">
              Stelle Fragen in natürlicher Sprache - erhalte präzise Daten-Insights
            </p>
          </div>

          <QueryInterface onQuery={handleQuery} isLoading={isLoading} />

          {results && <ResultsDisplay results={results} />}
        </main>
      </div>
    </div>
  );
}

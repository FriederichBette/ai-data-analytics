"use client";

import { useState } from "react";

interface QueryInterfaceProps {
    onQuery: (query: string) => void;
    isLoading: boolean;
}

export default function QueryInterface({ onQuery, isLoading }: QueryInterfaceProps) {
    const [query, setQuery] = useState("");

    const exampleQueries = [
        "Zeige mir die Top 10 Verkäufe im August sortiert nach Umsatz",
        "Welche Produkte haben die höchste Marge?",
        "Wie viele Kunden haben wir in Deutschland?",
        "Vergleiche Umsatz Q1 vs Q2 2024",
    ];

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (query.trim() && !isLoading) {
            onQuery(query);
        }
    };

    return (
        <div className="mb-8">
            <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-8 shadow-2xl border border-white/20">
                <form onSubmit={handleSubmit} className="space-y-4">
                    <div>
                        <label htmlFor="query" className="block text-sm font-medium text-gray-200 mb-2">
                            Deine Frage
                        </label>
                        <textarea
                            id="query"
                            value={query}
                            onChange={(e) => setQuery(e.target.value)}
                            placeholder="z.B. Zeige mir die Top 10 Verkäufe im August sortiert nach Umsatz"
                            className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all resize-none"
                            rows={3}
                            disabled={isLoading}
                        />
                    </div>

                    <button
                        type="submit"
                        disabled={isLoading || !query.trim()}
                        className="w-full bg-gradient-to-r from-purple-500 to-pink-500 text-white font-semibold py-3 px-6 rounded-xl hover:from-purple-600 hover:to-pink-600 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 focus:ring-offset-slate-900 disabled:opacity-50 disabled:cursor-not-allowed transition-all transform hover:scale-[1.02] active:scale-[0.98]"
                    >
                        {isLoading ? (
                            <span className="flex items-center justify-center">
                                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                                </svg>
                                Analysiere...
                            </span>
                        ) : (
                            "Abfrage starten"
                        )}
                    </button>
                </form>

                <div className="mt-6">
                    <p className="text-sm text-gray-300 mb-3">Beispiel-Abfragen:</p>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
                        {exampleQueries.map((example, index) => (
                            <button
                                key={index}
                                onClick={() => setQuery(example)}
                                className="text-left text-sm text-gray-300 bg-white/5 hover:bg-white/10 px-4 py-2 rounded-lg transition-all border border-white/10 hover:border-purple-500/50"
                                disabled={isLoading}
                            >
                                {example}
                            </button>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    );
}

"use client";

interface ResultsDisplayProps {
    results: {
        success: boolean;
        sql_query?: string;
        data?: any[];
        error?: string;
        row_count?: number;
    };
}

export default function ResultsDisplay({ results }: ResultsDisplayProps) {
    if (!results) return null;

    if (!results.success) {
        return (
            <div className="bg-red-500/10 backdrop-blur-lg rounded-2xl p-8 shadow-2xl border border-red-500/20">
                <div className="flex items-start">
                    <div className="flex-shrink-0">
                        <svg className="h-6 w-6 text-red-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                    </div>
                    <div className="ml-3">
                        <h3 className="text-lg font-medium text-red-300">Fehler</h3>
                        <p className="mt-2 text-sm text-red-200">{results.error}</p>
                    </div>
                </div>
            </div>
        );
    }

    return (
        <div className="space-y-6">
            {/* SQL Query Display */}
            {results.sql_query && (
                <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 shadow-2xl border border-white/20">
                    <h3 className="text-lg font-semibold text-white mb-3 flex items-center">
                        <svg className="w-5 h-5 mr-2 text-purple-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
                        </svg>
                        Generierte SQL-Abfrage
                    </h3>
                    <pre className="bg-slate-900/50 text-green-300 p-4 rounded-xl overflow-x-auto text-sm border border-white/10">
                        <code>{results.sql_query}</code>
                    </pre>
                </div>
            )}

            {/* Results Table */}
            {results.data && results.data.length > 0 && (
                <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 shadow-2xl border border-white/20">
                    <div className="flex items-center justify-between mb-4">
                        <h3 className="text-lg font-semibold text-white flex items-center">
                            <svg className="w-5 h-5 mr-2 text-purple-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                            </svg>
                            Ergebnisse
                        </h3>
                        <span className="text-sm text-gray-300 bg-white/5 px-3 py-1 rounded-full">
                            {results.row_count} {results.row_count === 1 ? "Zeile" : "Zeilen"}
                        </span>
                    </div>

                    <div className="overflow-x-auto">
                        <table className="w-full text-sm">
                            <thead>
                                <tr className="border-b border-white/10">
                                    {Object.keys(results.data[0]).map((key) => (
                                        <th
                                            key={key}
                                            className="text-left py-3 px-4 font-semibold text-purple-300 uppercase tracking-wider"
                                        >
                                            {key}
                                        </th>
                                    ))}
                                </tr>
                            </thead>
                            <tbody>
                                {results.data.map((row, index) => (
                                    <tr
                                        key={index}
                                        className="border-b border-white/5 hover:bg-white/5 transition-colors"
                                    >
                                        {Object.values(row).map((value: any, cellIndex) => (
                                            <td key={cellIndex} className="py-3 px-4 text-gray-200">
                                                {value === null || value === undefined
                                                    ? "-"
                                                    : typeof value === "object"
                                                        ? JSON.stringify(value)
                                                        : String(value)}
                                            </td>
                                        ))}
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            )}

            {results.data && results.data.length === 0 && (
                <div className="bg-yellow-500/10 backdrop-blur-lg rounded-2xl p-8 shadow-2xl border border-yellow-500/20 text-center">
                    <svg className="mx-auto h-12 w-12 text-yellow-400 mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
                    </svg>
                    <p className="text-yellow-300 text-lg">Keine Ergebnisse gefunden</p>
                    <p className="text-yellow-200/70 text-sm mt-2">Versuche eine andere Abfrage</p>
                </div>
            )}
        </div>
    );
}

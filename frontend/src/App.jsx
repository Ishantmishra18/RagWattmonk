import { useState } from "react";
import { askQuestion } from "./api";

function App() {
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    setLoading(true);
    setAnswer("");

    const data = await askQuestion(query);
    setAnswer(data.answer);

    setLoading(false);
  };

  return (
   <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 text-white">
  <div className="container mx-auto px-4 py-16">
    <div className="max-w-4xl mx-auto text-center">
      <h1 className="text-5xl md:text-7xl font-bold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-pink-400 to-purple-400">
        RAG Chatbot
      </h1>
      <p className="text-lg md:text-xl text-gray-300 mb-12 opacity-90">
        Ask anything. Get intelligent answers powered by retrieval-augmented generation.
      </p>

      <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-8 shadow-2xl border border-white/20">
        <textarea
          rows="4"
          id = "query"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask a question..."
          className="w-full p-4 rounded-lg bg-black/20 border border-white/30 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent resize-none"
        />
        
        <button
          onClick={handleAsk}
          className="mt-6 px-8 py-3 bg-gradient-to-r from-pink-500 to-purple-600 text-white font-semibold rounded-lg shadow-lg hover:from-pink-600 hover:to-purple-700 transform hover:scale-105 transition-all duration-200"
        >
          Ask
        </button>

        {loading && (
          <p className="mt-6 text-gray-300">Thinking...</p>
        )}

        {answer && (
          <div className="mt-8 p-6 bg-black/20 rounded-lg border border-white/10">
            <h4 className="font-semibold text-pink-400 mb-2">Answer</h4>
            <p className="text-gray-200">{answer}</p>
          </div>
        )}
      </div>
    </div>
  </div>
</div>   
  );
}

export default App;

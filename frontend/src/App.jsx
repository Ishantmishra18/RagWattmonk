import { useState } from "react";
import { askQuestion } from "./api";

function App() {
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setAnswer("");

    const data = await askQuestion(query);
    setAnswer(data.answer);

    setLoading(false);
    setQuery("");
  };

  // ✅ ENTER KEY SUPPORT
  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleAsk();
    }
  };

  return (
   <div className="min-h-screen bg-gradient-to-br from-slate-900 via-black to-slate-800 text-white">

      {/* INPUT BAR */}
      <div className="w-screen z-40 fixed bottom-0">
        <div className="textinput relative mx-64">
          <textarea
            rows="1"
            id="query"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={handleKeyDown}  
            placeholder="Ask a question..."
            className="w-full p-6 bg-neutral-700 rounded-[2vw] bg-black/20 outline-none focus:bg-border-white/20 resize-none"
          />
          <button
            onClick={handleAsk}
            className="absolute bottom-4 right-4 px-6 py-2 bg-gradient-to-r from-pink-500 to-purple-600 text-white font-semibold rounded-lg shadow-lg hover:from-pink-600 hover:to-purple-700 transform hover:scale-105 transition-all duration-200"
          >
            Ask
          </button>
        </div>
      </div>

      {/* CONTENT */}
      <div className="container mx-auto px-4 py-16">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-5xl md:text-7xl font-bold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-pink-400 to-purple-400">
            Wattmonk
          </h1>
          <p className="text-lg md:text-xl text-gray-300 mb-12 opacity-90">
            Ask any question about your documents and get instant answers powered by AI.
          </p>

          {/* ✅ NEW LOADING UI */}
          {loading && (
            <div className="mt-6 flex items-center justify-center gap-3 text-gray-300">
              <span>Thinking</span>
              <div className="loader-ball"></div>
            </div>
          )}

          {answer && (
            <div className="mt-8 p-6 bg-black/20 rounded-lg border border-white/10">
              <h4 className="font-semibold text-pink-400 mb-2">Answer</h4>
              <p className="text-gray-300">{answer}</p>
            </div>
          )}
        </div>
      </div>
   </div>
  );
}

export default App;

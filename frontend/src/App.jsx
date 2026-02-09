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
    <div style={{ padding: "40px", maxWidth: "700px", margin: "auto" }}>
      <h2>RAG Chatbot</h2>

      <textarea
        rows="4"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask a question..."
        style={{ width: "100%", padding: "10px" }}
      />

      <button
        onClick={handleAsk}
        style={{ marginTop: "10px", padding: "10px 20px" }}
      >
        Ask
      </button>

      {loading && <p>Thinking...</p>}

      {answer && (
        <div style={{ marginTop: "20px" }}>
          <h4>Answer</h4>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default App;

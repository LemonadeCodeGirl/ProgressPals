import React, { useState } from "react";

function App() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const handleSend = async () => {
    const res = await fetch("http://127.0.0.1:8000/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input }),
    });
    const data = await res.json();
    setResponse(data.choices[0].message.content);
  };

  return (
    <div>
      <h1>React + FastAPI + Groq</h1>
      <textarea value={input} onChange={e => setInput(e.target.value)} />
      <button onClick={handleSend}>Send</button>
      <p>Groq says: {response}</p>
    </div>
  );
}

export default App;
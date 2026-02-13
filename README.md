# ⚡ Wattmonk — AI Document Q&A System (RAG Powered)

Wattmonk is an AI-powered document question-answering system built using:

- 🧠 Retrieval Augmented Generation (RAG)
- 📄 PDF ingestion and chunking
- 🔎 ChromaDB vector database
- 🤖 Sentence Transformers embeddings
- 🚀 FastAPI backend
- ⚛️ React + Tailwind frontend

It allows users to upload documents and ask natural language questions to get accurate answers grounded in the document content.

---

# 📌 How It Works (Architecture Overview)

User Question  
↓  
React Frontend  
↓  
FastAPI Backend  
↓  
Embedding Generation (SentenceTransformers)  
↓  
ChromaDB Vector Search  
↓  
Relevant Context Retrieved  
↓  
LLM Generates Final Answer  
↓  
Response Sent to Frontend  

---

# 🧠 Core Concepts Used

## 1️⃣ RAG (Retrieval Augmented Generation)

Instead of training a model on documents, we:

1. Convert document text into vector embeddings.
2. Store them in a vector database.
3. When user asks a question:
   - Convert question into embedding.
   - Retrieve most similar chunks.
   - Send those chunks to LLM as context.
   - LLM generates grounded answer.

---

# 🗂 Project Structure

backend/
│
├── main.py
├── rag/
│ ├── vectorStore.py
│ ├── pdf_loader.py
│ ├── chunker.py
│
├── chroma_db/ (auto created)
│
frontend/
│
├── src/
│ ├── App.jsx
│ ├── api.js
│
└── package.json


---

# ⚙️ Backend Setup (FastAPI + Chroma)

## 1️⃣ Create Virtual Environment

```bash
cd backend
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.venv\Scripts\activate         # Windows
```

## 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

## 3️⃣ Run Backend Server
```
uvicorn main:app --reload
```
Server will run at:
http://127.0.0.1:8000

## 📥 Ingest Document
Open browser:
```
(http://127.0.0.1:8000/ingest_pdf
)
```

## 🔍 Verify Database
```
http://127.0.0.1:8000/count
```

Expected:

{
  "total_documents": 10957
}


# 🎨 Frontend Setup (React + Tailwind)
## 1️⃣ Install Dependencies
```
cd frontend
npm install
```

## 2️⃣ Start Frontend
```
npm run dev

```

# 🔐 Environment Variables

If using Gemini/OpenAI:

## Create .env file in backend:
```
GOOGLE_API_KEY=your_key_here
```

## Then access via:
```
import os
os.getenv("GOOGLE_API_KEY")
```





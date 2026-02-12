from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rag.vectorStore import ChromaVectorStore
from rag.retriever import retrieve
from rag.chunker import chunk_documents
from rag.generator import generate_answer
from rag.loader import load_docs

app = FastAPI()

# CORS (dev-friendly)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "Backend running"}

# ---------- RAG SETUP (runs once at startup) ----------

embedding = SentenceEmbedding()
vectorstore = VectorStore(embedding)

# Load & ingest documents (from Data folder)
docs = load_docs("Data/docs.txt")
chunks = chunk_documents(docs)
vectorstore.add_documents(chunks)

# ---------- API ----------

@app.get("/ask")
def ask(query: str):
    context = retrieve(vectorstore, query)
    answer = generate_answer(query, context)
    return {
        "query": query,
        "answer": answer,
        "context": context
    }

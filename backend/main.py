from fastapi import FastAPI
from Rag.vectorStore import VectorStore
from Rag.chunker import chunk_text
from Rag.embeddings import create_embedding
from Rag.retriever import retrieve
from Rag.generator import generate_answer
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

vectorstore = VectorStore(dim=384)

@app.post("/ingest")
def ingest(text: str):
    chunks = chunk_text(text)
    embeddings = [create_embedding(chunk) for chunk in chunks]
    vectorstore.add(embeddings, chunks)
    return {"status": "Document ingested"}

@app.get("/ask")
def ask(query: str):
    context = retrieve(query, vectorstore)
    answer = generate_answer(query, context)
    return {"answer": answer}

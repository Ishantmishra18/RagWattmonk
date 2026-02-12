from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from rag.loader import load_pdf
from rag.chunker import chunk_documents
from rag.vectorStore import ChromaVectorStore
from rag.retriever import retrieve
from rag.generator import generate_answer

app = FastAPI()

vectorstore = ChromaVectorStore()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "Backend running"}

@app.post("/ingest")
def ingest():
    documents = load_pdf("data/2017-NEC-Code-2.pdf")
    chunks = chunk_documents(documents)
    vectorstore.add_documents(chunks)
    return {"status": "NEC PDF ingested successfully"}

@app.get("/ask")
def ask(query: str):
    context = retrieve(query, vectorstore)
    answer = generate_answer(query, context)
    return {"answer": answer}

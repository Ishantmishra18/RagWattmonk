from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rag.vectorStore import ingest_pdf, retrieve
from rag.generator import generate_answer
from rag.vectorStore import get_collection

app = FastAPI()

# -----------------------------
# Enable CORS (for frontend)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Health Check
# -----------------------------
@app.get("/")
def health():
    return {"status": "Backend running successfully"}

# -----------------------------
# Ingest PDF (Run Once)
# -----------------------------

@app.get("/ingest_pdf")
def ingest():
    ingest_pdf("Data/main.pdf")  # Make sure path is correct
    return {"status": "PDF ingested successfully"}



@app.get("/count")
def count_documents():
    try:
        collection = get_collection()
        return {"total_documents": collection.count()}
    except Exception as e:
        return {"error": str(e)}



# -----------------------------
# Ask Question (RAG endpoint)
# -----------------------------
@app.get("/ask")
def ask(query: str):
    print("\n==============================")
    print("Incoming Query:", query)

    context = retrieve(query)
    print("Retrieved Context Length:", len(context))

    if not context:
        return {"answer": "No relevant context found in database."}

    answer = generate_answer(query, context)

    print("Generated Answer:", answer)
    print("==============================\n")

    return {"answer": answer}
 
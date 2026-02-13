import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from rag.pdf_loader import load_pdf
from rag.chunker import chunk_text

# Persistent Chroma client
chroma_client = chromadb.Client(
    Settings(
        persist_directory="./chroma_db",
        is_persistent=True
    )
)

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_collection():
    return chroma_client.get_or_create_collection(
        name="rag_collection"
    )


def ingest_pdf(file_path: str):
    print("Loading PDF...")
    text = load_pdf(file_path)
    print("PDF text length:", len(text))

    chunks = chunk_text(text)
    print("Total chunks created:", len(chunks))

    # Get collection FIRST
    collection = get_collection()

    # If already has documents, skip ingestion
    if collection.count() > 0:
        print("Collection already has documents. Skipping ingestion.")
        print("Current document count:", collection.count())
        return

    batch_size = 500

    for i in range(0, len(chunks), batch_size):
        batch_chunks = chunks[i:i+batch_size]
        embeddings = model.encode(batch_chunks).tolist()
        ids = [f"id_{j}" for j in range(i, i + len(batch_chunks))]

        collection.add(
            documents=batch_chunks,
            embeddings=embeddings,
            ids=ids
        )

        print(f"Inserted batch {i} to {i+len(batch_chunks)}")

    print("Final document count:", collection.count())



def retrieve(query: str, k: int = 3):
    collection = get_collection()

    if collection.count() == 0:
        print("No documents in DB")
        return ""

    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=k
    )

    documents = results.get("documents", [])

    if not documents or not documents[0]:
        return ""

    return " ".join(documents[0])

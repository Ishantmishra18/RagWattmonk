from sentence_transformers import SentenceTransformer

# Load embedding 
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embedding(text: str):
    """
    Converts text into a dense vector representation.
    """
    return embedding_model.encode(text)

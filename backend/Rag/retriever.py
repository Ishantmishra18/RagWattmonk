from rag.embeddings import create_embedding

def retrieve(query, vectorstore, k=3):
    """
    Finds the most relevant document chunks.
    """
    query_embedding = create_embedding(query)
    return vectorstore.search(query_embedding, k)

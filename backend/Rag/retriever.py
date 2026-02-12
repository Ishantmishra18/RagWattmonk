def retrieve(query: str, vectorstore, k: int = 3):
    results = vectorstore.search(query, k=k)
    return "\n".join(results)

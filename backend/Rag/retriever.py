def retrieve(query: str, vectorstore):
    results = vectorstore.search(query)
    return "\n".join(results)

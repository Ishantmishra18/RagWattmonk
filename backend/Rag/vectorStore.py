from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

class VectorStore:
    def __init__(self, persist_directory: str = "chroma_db"):
        """
        Initializes Chroma vector store with OpenAI embeddings
        """
        self.embedding_function = OpenAIEmbeddings()
        self.vectordb = Chroma(
            persist_directory=persist_directory,
            embedding_function=self.embedding_function
        )

    def add_texts(self, texts: list[str], metadatas: list[dict] | None = None):
        """
        Add documents to vector store
        """
        self.vectordb.add_texts(
            texts=texts,
            metadatas=metadatas
        )
        self.vectordb.persist()

    def similarity_search(self, query: str, k: int = 3):
        """
        Search similar documents
        """
        return self.vectordb.similarity_search(query, k=k)

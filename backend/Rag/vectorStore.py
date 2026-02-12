from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

class ChromaVectorStore:
    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        self.db = Chroma(
            collection_name="nec_collection",
            embedding_function=self.embedding_model,
            persist_directory="./chroma_db"
        )

    def add_documents(self, documents):
        self.db.add_documents(documents)

    def search(self, query, k=3):
        docs = self.db.similarity_search(query, k=k)
        return [doc.page_content for doc in docs]

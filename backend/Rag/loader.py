from langchain.document_loaders import TextLoader

def load_docs(path):
    loader = TextLoader(path, encoding="utf-8")
    return loader.load()

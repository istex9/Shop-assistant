import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents(directory_path):
    """
    Betölti az összes .txt fájlt a megadott könyvtárból.

    Args:
        directory_path (str): A dokumentumokat tartalmazó könyvtár elérési útja.

    Returns:
        list: A betöltött dokumentumok listája.
    """
    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory_path, filename)
            loader = TextLoader(filepath, encoding='utf-8')
            documents.extend(loader.load())
    return documents

def split_documents(documents):
    """
    Feldarabolja a dokumentumokat kisebb részekre a jobb kereshetőség érdekében.

    Args:
        documents (list): A betöltött dokumentumok listája.

    Returns:
        list: A feldarabolt dokumentumok listája.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)
    return docs

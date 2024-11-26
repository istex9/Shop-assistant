from vectorstore import load_vectorstore
from config import VECTORSTORE_PATH

def get_relevant_documents(query, k=4):
    """
    Lekéri a releváns dokumentumokat a vektortárból a felhasználói kérdés alapján.

    Args:
        query (str): A felhasználó kérdése.
        k (int): A visszaadandó dokumentumok száma.

    Returns:
        list: A releváns dokumentumok listája.
    """
    vectorstore = load_vectorstore(VECTORSTORE_PATH)
    docs = vectorstore.similarity_search(query, k=k)
    return docs

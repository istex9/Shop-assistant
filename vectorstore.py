from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from config import EMBEDDING_MODEL_NAME

def create_vectorstore(documents):
    """
    Létrehozza a vektortárat a dokumentumok alapján.

    Args:
        documents (list): A feldarabolt dokumentumok listája.

    Returns:
        FAISS: A létrehozott vektortár.
    """
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore

def save_vectorstore(vectorstore, path):
    """
    Elmenti a vektortárat a megadott útvonalra.

    Args:
        vectorstore (FAISS): A vektortár objektum.
        path (str): Az elérési út, ahova a vektortárat mentjük.
    """
    vectorstore.save_local(path)

def load_vectorstore(path):
    """
    Betölti a vektortárat a megadott útvonalról.

    Args:
        path (str): A vektortár elérési útja.

    Returns:
        FAISS: A betöltött vektortár.
    """
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    vectorstore = FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)
    return vectorstore

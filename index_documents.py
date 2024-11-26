from document_loader import load_documents, split_documents
from vectorstore import create_vectorstore, save_vectorstore
from config import DATA_PATH, VECTORSTORE_PATH

if __name__ == "__main__":
    print("Dokumentumok betöltése...")
    documents = load_documents(DATA_PATH)
    print(f"{len(documents)} dokumentum betöltve.")

    print("Dokumentumok feldarabolása...")
    docs = split_documents(documents)
    print(f"{len(docs)} darab dokumentumrészlet jött létre.")

    print("Vektortár létrehozása...")
    vectorstore = create_vectorstore(docs)
    print("Vektortár létrehozva.")

    print("Vektortár mentése...")
    save_vectorstore(vectorstore, VECTORSTORE_PATH)
    print(f"Vektortár elmentve a következő helyre: {VECTORSTORE_PATH}")

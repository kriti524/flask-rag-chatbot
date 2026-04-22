from rag import add_documents
import os

def ingest_folder(folder="docs/"):
    texts, ids = [], []
    for i, fname in enumerate(os.listdir(folder)):
        with open(os.path.join(folder, fname)) as f:
            texts.append(f.read())
            ids.append(f"doc_{i}")
    add_documents(texts, ids)
    print(f"Ingested {len(texts)} documents.")

if __name__ == "__main__":
    ingest_folder()
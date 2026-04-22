import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.get_or_create_collection("docs")

def add_documents(texts, ids):
    embeddings = model.encode(texts).tolist()
    collection.add(documents=texts, embeddings=embeddings, ids=ids)

def retrieve(query, top_k=3):
    embedding = model.encode([query]).tolist()
    results = collection.query(query_embeddings=embedding, n_results=top_k)
    return results["documents"][0]  # list of relevant chunks
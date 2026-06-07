import chromadb
import json
from pathlib import Path
from chromadb.utils import embedding_functions

# 1. Setup: Load the model specified in planning.md
MODEL_NAME = 'all-MiniLM-L6-v2'
CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "uc_merced_unofficial_guide"

# Path to your generated chunks
HERE = Path(__file__).parent
CHUNKS_JSON = HERE / 'documents' / 'data' / 'chunks.json'

# Initialize ChromaDB client and Embedding Function
client = chromadb.PersistentClient(path=str(HERE / CHROMA_PATH))
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=MODEL_NAME
)

# Get or create the collection
collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_func,
    metadata={"hnsw:space": "cosine"}
)

def ingest_chunks():
    """
    Reads chunks.json and loads them into ChromaDB with metadata.
    """
    if collection.count() > 0:
        print(f"Vector store already populated with {collection.count()} chunks.")
        return

    if not CHUNKS_JSON.exists():
        print(f"Error: {CHUNKS_JSON} not found. Run load_documents.py first.")
        return

    with open(CHUNKS_JSON, 'r', encoding='utf-8') as f:
        chunks = json.load(f)

    print(f"Ingesting {len(chunks)} chunks into ChromaDB...")
    
    collection.add(
        documents=[c['chunk_text'] for c in chunks],
        metadatas=[{
            "source": c['source_path'],
            "index": c['chunk_index']
        } for c in chunks],
        ids=[f"id_{i}" for i in range(len(chunks))]
    )
    print("Ingestion complete.")

def retrieve_relevant_chunks(query, k=5):
    """
    Given a user query, returns the top k most semantically similar chunks.
    """
    results = collection.query(
        query_texts=[query],
        n_results=k,
        include=["documents", "metadatas", "distances"]
    )
    
    # Reformat for easier use in generation
    output = []
    for i in range(len(results['documents'][0])):
        output.append({
            "text": results['documents'][0][i],
            "metadata": results['metadatas'][0][i],
            "score": results['distances'][0][i]
        })
    return output

if __name__ == "__main__":
    ingest_chunks()
    test_query = "What is the workload for CSE 100?"
    hits = retrieve_relevant_chunks(test_query)
    for hit in hits:
        print(f"\n[Score: {hit['score']:.4f}] Source: {hit['metadata']['source']}")
        print(f"Content: {hit['text'][:100]}...")

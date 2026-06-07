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

    Tuning k is critical for RAG performance:
    - Too few chunks: Risk missing the answer entirely.
    - Too many chunks: Risk diluting context and distracting the LLM.
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
            "distance": results['distances'][0][i]  # Lower distance = higher similarity
        })
    return output

if __name__ == "__main__":
    ingest_chunks()

    # Test queries from planning.md Evaluation Plan
    eval_queries = [
        "How was the CSE 100 workload in Spring 2026?",
        "What is the hardest CSE course in the UC Merced?",
        "Should CS in UC Merced has to be considered as a bad choice?"
    ]

    for query in eval_queries:
        print(f"\n{'='*20} TESTING EVALUATION QUERY {'='*20}")
        print(f"Query: {query}")
        
        hits = retrieve_relevant_chunks(query, k=5)
        for hit in hits:
            print(f"\n[Distance: {hit['distance']:.4f}] Source: {hit['metadata']['source']}")
            print(f"Content: {hit['text'][:250]}...")
        
        print(f"\nQUESTION: Are these results actually relevant to the query: '{query}'?")

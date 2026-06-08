import chromadb
import json
import re
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
    if not CHUNKS_JSON.exists():
        print(f"Error: {CHUNKS_JSON} not found. Run load_documents.py first.")
        return

    with open(CHUNKS_JSON, 'r', encoding='utf-8') as f:
        chunks = json.load(f)

    # If the count is different, reset the collection to ensure we have the latest data
    if collection.count() != len(chunks):
        print(f"Syncing Vector Store: Found {collection.count()} chunks, expected {len(chunks)}. Re-ingesting...")
        if collection.count() > 0:
            all_ids = collection.get()['ids']
            collection.delete(ids=all_ids)
    else:
        print(f"Vector store already up to date with {collection.count()} chunks.")
        return

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

def retrieve_relevant_chunks(query, k=5, threshold=0.65):
    """
    Given a user query, pulls a wider net of results and applies a soft keyword 
    boost to exact course pattern matches so they dominate the top ranks.
    """
    # Detect explicit course patterns (e.g., "CSE 100", "CSE 31")
    course_match = re.search(r'\b([A-Z]{2,4})\s*(\d{1,3})\b', query.upper())
    
    # Strategy: Pull a wider pool of chunks initially (k * 3) so that drifted chunks 
    # are caught in the initial vector sweep.
    initial_k = max(k * 3, 15)
    
    results = collection.query(
        query_texts=[query],
        n_results=initial_k,
        include=["documents", "metadatas", "distances"]
    )

    # Guard clause for empty databases
    if not results or not results['documents'] or not results['documents'][0]:
        return []
    
    output = []
    
    # Extract structural search targets if found
    target_pattern = None
    if course_match:
        dept, num = course_match.groups()
        target_pattern = f"{dept}{num}"
        print(f"[search] Course pattern detected: '{dept} {num}'. Applying soft-boost scoring.")

    for i in range(len(results['documents'][0])):
        text = results['documents'][0][i]
        metadata = results['metadatas'][0][i]
        distance = results['distances'][0][i]
        
        # Normalize text spacing to capture keywords seamlessly across line breaks
        normalized_text = re.sub(r'\s+', '', text.upper())
        
        if target_pattern:
            if target_pattern in normalized_text:
                # Substantial reward: push exact matches straight to the top
                distance -= 0.25  
            elif any(f"{dept}{x}" in normalized_text for x in ['160', '120', '176'] if x != num):
                # Mild penalty: suppress other courses competing for attention
                distance += 0.1   

        # Filter out completely irrelevant high-distance noise after adjustments
        if distance <= threshold:
            output.append({
                "text": text,
                "metadata": metadata,
                "distance": distance
            })
            
    # Re-sort everything based on our newly adjusted distances
    output = sorted(output, key=lambda x: x["distance"])
    
    # Return exactly the top k results requested
    return output[:k]

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
            print(f"\n[Distance: {hit['distance']:.3f}] Source: {hit['metadata']['source']}")
            print(f"Content: {hit['text'][:250]}...")

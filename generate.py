import os
from dotenv import load_dotenv
from groq import Groq
from retrieval import ingest_chunks, retrieve_relevant_chunks

# Setup: load the Groq key from .env and connect to the LLM
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL_NAME = "llama-3.3-70b-versatile"

SYSTEM_PROMPT = (
    "You are an unofficial guide to UC Merced CSE courses and professors. "
    "Answer ONLY using the numbered context below. "
    "Cite the sources you use with their [number]. "
    "If the context does not contain the answer, say so — do not invent facts."
)


def _generate(query, k=8):
    """
    Core RAG step: retrieve the top-k chunks, ground them as context, and ask
    the Groq LLM for a cited answer. Returns (answer_text, hits).
    """
    hits = retrieve_relevant_chunks(query, k=k)

    if not hits:
        return "I don't have enough information in my sources to answer that.", []

    # Build a numbered context block so the model can cite by [number]
    context = "\n\n".join(
        f"[{i+1}] (source: {h['metadata']['source']})\n{h['text']}"
        for i, h in enumerate(hits)
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"},
        ],
        temperature=0.2,  # low temperature keeps the answer grounded in the chunks
    )
    return response.choices[0].message.content, hits


def ask(query, k=8):
    """
    Structured result for the query interface (app.py):
    {"answer": <model text>, "sources": [unique source documents]}.
    """
    answer, hits = _generate(query, k=k)

    # Deduplicate sources while preserving retrieval order
    sources = []
    for h in hits:
        src = h["metadata"]["source"]
        if src not in sources:
            sources.append(src)

    return {"answer": answer, "sources": sources}


def generate_answer(query, k=8):
    """
    CLI helper: the model answer with a numbered Sources block appended.
    Numbers match the [number] citations in the context block.
    """
    answer, hits = _generate(query, k=k)
    if not hits:
        return answer

    sources_block = "\n".join(
        f"  [{i+1}] {h['metadata']['source']}" for i, h in enumerate(hits)
    )
    return f"{answer}\n\nSources:\n{sources_block}"


if __name__ == "__main__":
    ingest_chunks()

    # Test questions from planning.md Evaluation Plan
    eval_queries = [
        "How was the CSE 100 workload in Spring 2026?",
        "What is the hardest CSE course in the UC Merced?",
        "Should CS in UC Merced has to be considered as a bad choice?",
        "How was the professor Santosh Chandrasekhar's grading policy in CSE 31?",
        "What do students say about the quality of CS classes in UC Merced?",
    ]

    for query in eval_queries:
        print(f"\n{'='*25} QUERY {'='*25}")
        print(f"Q: {query}\n")
        print(generate_answer(query))

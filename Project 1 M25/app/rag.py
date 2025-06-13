
import numpy as np
from embed import load_embeddings, load_metadata
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("AIPROXY_TOKEN"),
    base_url="https://aiproxy.sanand.workers.dev/openai/v1"
)

embeddings = load_embeddings()
metadata = load_metadata()

def embed_text(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=[text]
    )
    return np.array(response.data[0].embedding, dtype='float32')

def retrieve_relevant_chunks(query_embedding, top_k=5):
    distances = np.linalg.norm(embeddings - query_embedding, axis=1)
    top_k_idx = distances.argsort()[:top_k]

    results, sources = [], []

    for i in top_k_idx:
        m = metadata[i]
        source_type = m.get("source_type", "course")

        if source_type == "course":
            chunk_text = f"- {m['chunk']} (Source: {m['source']})"
            link = {"url": m["source"], "text": m["chunk"][:80] + "..."}
        elif source_type == "discourse":
            full_url = m["source"]
            chunk_text = f"- {m['chunk']} (Post: {full_url})"
            link = {"url": full_url, "text": m["chunk"][:80] + "..."}
        else:
            chunk_text = f"- {m['chunk']} (Unknown Source)"
            link = {"url": "", "text": m["chunk"][:80] + "..."}

        results.append(chunk_text)
        sources.append(link)

    return results, sources

def answer_question(question):
    query_embedding = embed_text(question)
    relevant_chunks, links = retrieve_relevant_chunks(query_embedding)

    prompt = f"""
You are a helpful Virtual TA for the TDS course.

Answer the student's query below, using only the provided context.

Query: {question}

Relevant Context:
{chr(10).join(relevant_chunks)}

Always include helpful explanations, but only based on the context provided. Include source references when useful.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful virtual TA for the TDS course."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip(), links

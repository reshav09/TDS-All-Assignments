import chromadb
from chromadb.utils import embedding_functions
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from sentence_transformers import SentenceTransformer
import os

# Initialize FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for internal portal)
    allow_credentials=True,
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["*"]
)

# Request model
class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str

# Response model
class SimilarityResponse(BaseModel):
    matches: List[str]

# Setup ChromaDB client and collection
async def setup_vector_db():
    """Initialize Chroma DB with an embedding function."""
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="BAAI/bge-base-en-v1.5"
    )
    client = chromadb.PersistentClient(path="./vector_db")
    collection = client.create_collection(
        name="documents",
        embedding_function=sentence_transformer_ef
    )
    return collection

# Setup vector database
collection = setup_vector_db()

# Endpoint to process documents and search queries
@app.post("/similarity", response_model=SimilarityResponse)
async def similarity_endpoint(payload: SimilarityRequest):
    # Compute embeddings for the documents and query
    query_embedding = collection.get_embedding(payload.query)
    doc_embeddings = [collection.get_embedding(doc) for doc in payload.docs]

    # Calculate cosine similarity for each document
    similarities = [
        cosine_similarity(query_embedding, doc_emb) for doc_emb in doc_embeddings
    ]

    # Sort and get the top 3 similar documents
    ranked_indices = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)
    top_matches = [payload.docs[i] for i in ranked_indices[:3]]

    return {"matches": top_matches}

def cosine_similarity(vec1, vec2):
    a = np.array(vec1)
    b = np.array(vec2)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))



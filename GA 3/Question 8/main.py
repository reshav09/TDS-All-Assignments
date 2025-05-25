from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import httpx
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Initialize FastAPI app
app = FastAPI()

# Configuration - API Token and URL for embedding service
API_TOKEN = "Your-Token"  # Replace with your token
EMBEDDING_SERVICE_URL = "http://aiproxy.sanand.workers.dev/openai/v1/embeddings"
EMBEDDING_MODEL_NAME = "text-embedding-3-small"

# CORS middleware for development purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (adjust for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data models for request and response
class SimilarityQuery(BaseModel):
    documents: List[str]
    query_text: str
    top_results: Optional[int] = 3  # Default to top 3 similar documents

class SimilarityOutcome(BaseModel):
    documents: List[str]
    scores: List[float]  # List of similarity scores corresponding to each document

# Fetch embeddings for the given text input
async def fetch_embeddings(texts: List[str]) -> List[List[float]]:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                EMBEDDING_SERVICE_URL,
                headers={
                    "Authorization": f"Bearer {API_TOKEN}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": EMBEDDING_MODEL_NAME,
                    "input": texts
                }
            )
            response.raise_for_status()  # Raise error if the request fails
            data = response.json()  # Parse the response JSON
            return [item['embedding'] for item in data['data']]  # Return the embeddings
        except httpx.HTTPStatusError as error:
            raise HTTPException(status_code=error.response.status_code, detail=f"Embedding service error: {str(error)}")
        except Exception as error:
            raise HTTPException(status_code=500, detail=f"Error in embedding fetch: {str(error)}")

# API endpoint to compute similarity between query and documents
@app.post("/similarity", response_model=SimilarityOutcome)
async def calculate_similarity(query: SimilarityQuery):
    if not query.documents:
        raise HTTPException(status_code=400, detail="Documents list cannot be empty.")
    if not query.query_text:
        raise HTTPException(status_code=400, detail="Query text cannot be empty.")

    try:
        # Fetch embeddings for both the query and the documents
        document_embeddings = await fetch_embeddings(query.documents)
        query_embedding = await fetch_embeddings([query.query_text])

        # Calculate cosine similarities between the query and document embeddings
        similarity_scores = cosine_similarity(query_embedding, document_embeddings)[0]

        # Determine the top N similar documents (sorted by similarity score)
        top_n = min(query.top_results, len(query.documents))
        sorted_indices = np.argsort(similarity_scores)[-top_n:][::-1]

        # Prepare the list of the most similar documents and their corresponding similarity scores
        similar_documents = [query.documents[i] for i in sorted_indices]
        similarity_values = [similarity_scores[i] for i in sorted_indices]

        return SimilarityOutcome(documents=similar_documents, scores=similarity_values)

    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(error)}")

# To run the app locally (for development)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)


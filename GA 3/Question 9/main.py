from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
import logging
import json

# Mock data simulating content from the TypeScript Book
# In a real RAG system, you'd index and retrieve from an actual corpus
DOCUMENT_EXCERPTS = [
    {
        "text": "The fat arrow (=>) is used to define arrow functions. The author affectionately calls it the fat arrow.",
        "source": "https://github.com/basarat/typescript-book/blob/master/docs/functions.md"
    },
    {
        "text": "!! is a double NOT operator in JavaScript and TypeScript, used to convert any value to its boolean equivalent.",
        "source": "https://github.com/basarat/typescript-book/blob/master/docs/javascript/boolean.md"
    },
    # Add more relevant excerpts here...
]

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple keyword-based retrieval
def find_answer(query: str):
    for doc in DOCUMENT_EXCERPTS:
        if any(kw.lower() in doc["text"].lower() for kw in query.lower().split()):
            return {
                "answer": doc["text"],
                "sources": doc.get("source", "")
            }
    return {
        "answer": "Sorry, no relevant information was found in the TypeScript Book.",
        "sources": None
    }

@app.get("/search")
async def search_documentation(q: str = Query(..., description="The documentation question to answer")):
    logger.debug(f"Received query: {q}")
    result = find_answer(q)
    logger.debug(f"Search result: {result}")
    return result

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting server at http://127.0.0.1:8810")
    uvicorn.run(app, host="127.0.0.1", port=8810, log_level="debug")


### `steps for similarity-api`

````markdown
# Similarity API Documentation

This API provides a service to calculate the similarity between a user query and a list of documents. It uses embeddings generated from OpenAI models and calculates the cosine similarity between the query and each document. The results include the most similar documents along with their similarity scores.

## Endpoints

### `/similarity`
This endpoint receives a request with documents and a query, and returns the top N most similar documents to the query based on cosine similarity.

#### Method: `POST`

#### Request Body

The request body should contain the following JSON structure:

```json
{
  "documents": [
    "First document content.",
    "Second document content.",
    "Third document content."
  ],
  "query_text": "Query for finding similar documents.",
  "top_results": 2
}
````

##### Parameters:

* `documents` (required): A list of documents (strings) to compare against the query.
* `query_text` (required): The query text to be compared to the documents.
* `top_results` (optional): The number of top similar documents to return (default is `3`).

#### Response Body

The response body will return the top N most similar documents along with their similarity scores:

```json
{
  "documents": [
    "Second document content.",
    "First document content."
  ],
  "scores": [
    0.92,
    0.85
  ]
}
```

##### Response Fields:

* `documents`: A list of the most similar documents, sorted by similarity.
* `scores`: A list of cosine similarity scores corresponding to each document in the `documents` array.

#### Error Responses

* **400 Bad Request**: If no documents or an empty query is provided, a `400` error will be returned.

  ```json
  {
    "detail": "Documents list cannot be empty."
  }
  ```

* **500 Internal Server Error**: If an unexpected error occurs (e.g., embedding service failure), a `500` error will be returned.

  ```json
  {
    "detail": "Internal error: {error_message}"
  }
  ```

## Example Usage

### Example Request

Here is an example of how to call the `/similarity` endpoint:

```bash
curl -X 'POST' \
  'http://127.0.0.1:5000/similarity' \
  -H 'Content-Type: application/json' \
  -d '{
  "documents": [
    "First document content.",
    "Second document content.",
    "Third document content."
  ],
  "query_text": "Query for finding similar documents.",
  "top_results": 2
}'
```

### Example Response

The API will return the most similar documents along with their similarity scores:

```json
{
  "documents": [
    "Second document content.",
    "First document content."
  ],
  "scores": [
    0.92,
    0.85
  ]
}
```

## API Structure

### FastAPI App

* The app is built using [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance) web framework for building APIs with Python 3.7+.
* The app includes CORS middleware to support cross-origin requests for development purposes.

### Request and Response Models

* **SimilarityQuery (Request Model)**:

  * `documents` (List of str): The list of documents to compare against.
  * `query_text` (str): The query string to compare against the documents.
  * `top_results` (Optional\[int], default: 3): The number of top similar documents to return.

* **SimilarityOutcome (Response Model)**:

  * `documents` (List of str): The list of most similar documents.
  * `scores` (List of float): The cosine similarity scores corresponding to each document.

### Helper Functions

* **`fetch_embeddings(texts: List[str])`**: This function sends a request to an embedding service to fetch the embeddings for the provided texts (documents and query).

* **`calculate_similarity(query: SimilarityQuery)`**: This endpoint processes the query and documents, fetches the embeddings, calculates cosine similarities, and returns the top N most similar documents.

## Installation and Setup

To run this API locally, follow these steps:

1. Clone this repository or create a new Python environment.

2. Install the required dependencies:

   ```bash
   pip install fastapi uvicorn httpx scikit-learn
   ```

3. Save the code in a Python file (e.g., `main.py`).

4. Run the FastAPI app:

   ```bash
   uvicorn main:app --reload
   ```

5. Access the API at `http://127.0.0.1:5000`.

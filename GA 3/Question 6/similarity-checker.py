import requests
import base64
import numpy as np

def calculate_similarity_score():
    # Step 1: Get user inputs
    # Prompt user to enter their API key, image file path, and a text description.
    api_key = input("Enter your API key: ")  # API key for authenticating with the service
    image_path = input("Enter the path to your image file: ")  # Path to the image file
    text_description = input("Enter the text description: ")  # Text description for comparison
    
    # Step 2: Read and encode the image
    # Attempt to read and encode the image as base64
    try:
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        # Error message if the image file is not found
        print(f"Error: Image file not found at {image_path}")
        return
    
    # Step 3: Prepare the API request payload
    # Define the URL for the API and set the headers with the API key for authorization
    url = "https://api.jina.ai/v1/embeddings"  # The endpoint URL for making the request
    headers = {
        "Authorization": f"Bearer {api_key}",  # Pass the API key for authorization
        "Content-Type": "application/json"  # Indicate the payload type is JSON
    }
    
    # Prepare the payload with the model name, text, and encoded image
    payload = {
        "model": "jina-clip-v2",  # Model name, change this if using a different model
        "input": [
            {"text": text_description},  # Text description to be embedded
            {"image": encoded_image}  # Encoded image to be embedded
        ]
    }
    
    # Step 4: Send the API request
    # Make a POST request to the API
    print("Sending request to Jina AI...")
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        
        # Step 5: Process the response data
        # Parse the JSON response and extract the embeddings
        data = response.json()
        
        # Extract embeddings for both text and image
        text_embedding = np.array(data["data"][0]["embedding"])
        image_embedding = np.array(data["data"][1]["embedding"])
        
        # Step 6: Calculate similarity using cosine similarity (dot product of normalized vectors)
        similarity_score = np.dot(text_embedding, image_embedding)  # Cosine similarity calculation
        
        # Print the similarity score rounded to 6 decimal places
        print(f"\nSimilarity score: {similarity_score:.6f}")
        return similarity_score
        
    except requests.exceptions.RequestException as e:
        # Handle request errors, such as network issues or invalid responses
        print(f"Error making API request: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response status: {e.response.status_code}")
            print(f"Response text: {e.response.text}")
    except Exception as e:
        # General error handler for other exceptions
        print(f"An error occurred: {e}")

# Step 7: Call the function to calculate similarity
# This is where the main program starts executing
if __name__ == "__main__":
    calculate_similarity_score()  # Call the function to start the process


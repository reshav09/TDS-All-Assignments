import httpx
import json

# Custom endpoint and headers
url = "https://aipipe.org/openai/v1/responses"
headers = {
    "Authorization": "Bearer Your-PipiAI-Token",  # Replace with your actual API key
    "Content-Type": "application/json"
}

# The exact message for the test case
user_message = """ Your Message Here"""# Send this message as the input.

# Adjusted payload for custom API (ensure this matches the custom API's required format)
payload = {
    "model": "gpt-4.1-nano",  # Model for testing, replace if necessary
    "input": user_message  # The user input message, using "input" key as in the working script
}

# Send POST request and handle errors
try:
    # Make the POST request to the custom API
    response = httpx.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Check if the request was successful

    # Extract response data
    data = response.json()

    # Print response data (if available)
    print(f"Response Data: {json.dumps(data, indent=2)}")

    # Assuming the token usage is similar to the working script:
    print("Input Tokens:", data["usage"]["input_tokens"])  # Adjust depending on API response structure

except httpx.RequestError as e:
    print(f"An error occurred while sending the request: {e}")
except httpx.HTTPStatusError as e:
    print(f"HTTP error occurred: {e}")


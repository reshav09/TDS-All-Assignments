import json

# Replace with your actual base64 image string
image_base64 = "Paste your URL here"  # URL for the image or the base64 encoded image string

# Prepare the JSON payload
payload = {
    "model": "gpt-4o-mini",  # Change the model if needed (e.g., "gpt-4" or "text-davinci-003")
    "messages": [
        {
            "role": "user",  # Set the role to "user" to simulate user input
            "content": [
                {
                    "type": "text",  # Indicates that this message is of type 'text'
                    "text": "Extract text from this image."  # User request message
                },
                {
                    "type": "image_url",  # Type indicating that the content is an image URL
                    "image_url": {"url": f"{image_base64}"}  # Image URL (could be base64 encoded or direct URL)
                }
            ]
        }
    ]
}

# Print the JSON payload
# This prints the formatted JSON, making it easier to review and debug
print(json.dumps(payload, indent=2))


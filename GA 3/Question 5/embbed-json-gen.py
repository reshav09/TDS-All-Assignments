import json

# Step 1: Define the input messages
# You can change these messages to suit your needs, e.g., different sentences or variables.
message_1 = "First Text"  # First message to be processed
message_2 = "Second Text"  # Second message to be processed

# Step 2: Prepare the JSON payload
# This payload structure is used to send the input messages to the model.
# You can change the model name to any available model as needed, e.g., "text-davinci-003".
payload = {
    "model": "text-embedding-3-small",  # The model you want to use for processing. Adjust the model name if necessary.
    "input": [message_1, message_2]    # The input messages are provided here as an array. You can add more messages if needed.
}

# Step 3: Print the JSON payload
# This will print the JSON payload with indentation for easy readability.
# You can use this payload in your API requests.
print(json.dumps(payload, indent=2))


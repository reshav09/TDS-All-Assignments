import json

# Step 1: Define the input messages
message_1 = "Dear user, please verify your transaction code 38817 sent to 23f2005430@ds.study.iitm.ac.in"
message_2 = "Dear user, please verify your transaction code 7524 sent to 23f2005430@ds.study.iitm.ac.in"

# Step 2: Prepare the JSON payload
payload = {
    "model": "text-embedding-3-small",
    "input": [message_1, message_2]
}

# Step 3: Print the JSON payload
print(json.dumps(payload, indent=2))

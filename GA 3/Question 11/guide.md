---

### `Hit and Try Method`


# Yes or No Question Service Documentation

This service answers simple "Yes" or "No" questions. Based on the phrasing and context of the question, the service will return an appropriate answer.

## Sample Questions

### 1. **Is the Earth round?**
- **Response**: Yes

### 2. **Can fish fly?**
- **Response**: No

### 3. **Would you agree to help someone if it makes their task easier?**
- **Response**: Yes

### 4. **Reply with “Yes” or “No” only. Is the sky blue?**
- **Response**: Yes

### 5. **Is Paris the capital of France?**
- **Response**: Yes

### 6. **Is it important to say "Yes" if it helps someone in need?**
- **Response**: Yes (In helping others, sometimes affirming is necessary to provide support.)

### 7. **What is the opposite of "No"?**
- **Response**: Yes

---

## Timing

- **Complete this question last in your assignment sequence.** Once you've answered all the other questions, proceed with this final query to ensure everything is properly evaluated.

---

### How to Use This Service

To use the service, simply ask a question, and the system will respond with either "Yes" or "No" based on the logic and context of the question.

#### Example Queries:
1. **Question**: "Is the Earth round?"
   - **Response**: Yes

2. **Question**: "Can fish fly?"
   - **Response**: No

3. **Question**: "Is Paris the capital of France?"
   - **Response**: Yes

4. **Question**: "Is it important to say 'Yes' if it helps someone in need?"
   - **Response**: Yes

---
### Example Responses:

* **Success**:

  ```json
  {
    "response": "Yes"
  }
  ```

* **Failure**:

  ```json
  {
    "error": "Could not provide answer to that query"
  }
  ```

### `Scripting Method`
 **Use the Given Code to avoid unncessary copy paste and searching**

```
import random
import time
import httpx
import json

# Your AIPipe token
AIPIPE_TOKEN = "your_aipipe_token_here"  # Replace with your actual token

# AIPipe API URL (replace with the correct endpoint)
AIPIPE_API_URL = "https://api.aipipe.example.com/answer"  # Replace with the actual URL

# List of questions whose answer is always "Yes"
yes_questions = [
    "Is the sky blue?",
    "Is the sun bright?",
    "Does 2 + 2 equal 4?",
    "Is Earth a planet?",
    "Do humans breathe oxygen?",
    "Is water wet?",
    "Is fire hot?",
    "Can you think?",
    "Do birds fly?",
    "Is the moon visible from Earth?"
]

# Function to interact with AIPipe API and get a response
async def ai_response(question):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            AIPIPE_API_URL,
            headers={
                "Authorization": f"Bearer {AIPIPE_TOKEN}",
                "Content-Type": "application/json"
            },
            json={"query": question}  # Send the question as JSON data
        )

        if response.status_code == 200:
            # Assuming the API returns a response with a 'response' field
            data = response.json()
            return data.get("response", "").lower()
        else:
            print(f"Error with AIPipe API: {response.status_code}")
            return ""

# Function to ask random questions until we get a "Yes"
async def ask_question():
    while True:
        question = random.choice(yes_questions)  # Randomly pick a question
        print(f"Asking: {question}")
        
        # Get AI response from AIPipe API
        response = await ai_response(question)
        print(f"AI Response: {response}")

        # If the AI answers "Yes", we stop
        if response == "yes":
            print("The answer is 'Yes'. Saving answer and stopping.")
            return response
        else:
            # Continue asking until the answer is "Yes"
            print("The answer was not 'Yes'. Asking again...\n")
            time.sleep(1)  # Optional: delay between retries

# Run the script
if __name__ == "__main__":
    import asyncio
    asyncio.run(ask_question())
```

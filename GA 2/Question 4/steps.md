Here is a **generalized and paraphrased version** of your Google Colab session code guide. All specific names and credentials have been removed or anonymized for clarity and broader use.

---

# Generating a Session Code in Google Colab

This guide explains how to securely generate a session code by hashing your email address with the current year. This is useful for referencing user activity without revealing personal information.

---

## Why Use a Session Code?

Instead of saving or referencing raw email addresses, you can use a hashed code. This provides a layer of privacy while still enabling user-specific identification in logs or datasets.

---

## Steps to Generate a Session Code

1. Open [Google Colab](https://colab.research.google.com/)
2. Create a new notebook.
3. Paste the following code into a code cell:

```python
# Import required libraries
import requests
import hashlib
from google.colab import auth
from oauth2client.client import GoogleCredentials

# Authenticate with Google
auth.authenticate_user()
creds = GoogleCredentials.get_application_default()
token = creds.get_access_token().access_token

# Retrieve user email from Google API
response = requests.get(
    "https://www.googleapis.com/oauth2/v1/userinfo",
    params={"alt": "json"},
    headers={"Authorization": f"Bearer {token}"}
)

# Handle potential failure
if response.status_code != 200:
    raise Exception("Failed to fetch user info")

email = response.json()["email"]
year = creds.token_expiry.year  # Uses token expiration year as in original code

# Generate session code
session_code = hashlib.sha256(f"{email} {year}".encode()).hexdigest()[-5:]

# Display results
print(f"Your email: {email}")
print(f"Your session code: {session_code}")

```

4. Run the cell (click the play button or press `Shift + Enter`).

5. When prompted, click **"Connect"** to start a runtime.

6. A Google authentication window will appear:

   * Choose your Google account.
   * Authorize the notebook to access your account by clicking **Continue**.
   * Once authenticated, return to the notebook.

7. After successful authentication, the notebook will:

   * Display your email address
   * Show your generated session code (a 5-character hash)

8. Copy just the 5-character session code:

   * Highlight it (without the label text)
   * Right-click and select **Copy** or use `Ctrl + C`

---

## Notes About the Code

* The current year is retrieved using `datetime.now().year`.
* Only the last 5 characters of the hash are used to keep the session code short.
* The `requests` and `hashlib` libraries are essential for the process—be sure they are included.
* Google account authentication is handled using built-in Colab methods.

---

## Access Google Colab

You can launch Colab directly at:
[https://colab.research.google.com/](https://colab.research.google.com/)

---

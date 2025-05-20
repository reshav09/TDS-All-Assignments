---

# Implementing Google SSO with FastAPI

This guide walks you through setting up a FastAPI application with Google Single Sign-On (SSO) authentication, exposing the user's ID token.

---

## IMPORTANT: Token Expiry Warning

**Google ID tokens expire after 1 hour. Ensure you complete the assignment and submit within this time frame. If necessary, restart the server before submitting.**

---

## Project Overview

You’ll build a FastAPI application that:

* Redirects unauthenticated users to Google's login page
* Handles OAuth callback and token exchange
* Stores the ID token in the session
* Exposes an endpoint to get the raw ID token

---

## Step 1: Set Up Project Structure

Create the following structure:

```
google-sso-api/
├── app.py          # FastAPI application
├── .env            # Environment variables (not committed to version control)
└── requirements.txt # Project dependencies
```

---

## Step 2: Create the Requirements File

Create a file named `requirements.txt` with the following content:

```
fastapi
uvicorn
python-dotenv
authlib
httpx
itsdangerous
```

---

## Step 3: Install Dependencies

Run the following in your terminal:

```
pip install -r requirements.txt
```

---

## Step 4: Set Up Google OAuth Credentials

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Navigate to "APIs & Services" > "Credentials".
4. Click "Create Credentials" > "OAuth client ID".
5. Select "Web application" as the application type.
6. Add a name for your OAuth client.
7. Under "Authorized redirect URIs", add:

   * `http://localhost:5000/`
   * `http://127.0.0.1:5000/`
   * `http://localhost:5000/auth/callback`
   * `http://127.0.0.1:5000/auth/callback`
8. Click "Create".
9. Copy the **Client ID** and **Client Secret**.

---

## Step 5: Create the Environment File

Create a `.env` file with the following content (replace with your credentials):

```
GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-client-secret
```

---

## Step 6: Create the FastAPI Application

Create `app.py` with the following content:

```python
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Add session middleware for storing user info
app.add_middleware(SessionMiddleware, secret_key="your-secret-key-here")

# Configure OAuth client for Google
oauth = OAuth()
oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

@app.get("/")
async def home(request: Request):
    """
    Main route that handles:
    1. Initial redirect to Google login for unauthenticated users
    2. Processing the callback from Google authentication
    3. Displaying status for authenticated users
    """
    user = request.session.get("user")
    
    # For authenticated users, show success message
    if user:
        return {"message": "You are logged in", "email": user.get("email")}
    
    # For users who have just logged in, save their details in the session
    if "code" in request.query_params:
        token = await oauth.google.authorize_access_token(request)
        request.session["user"] = token.get("userinfo")
        request.session["id_token"] = token.get("id_token")
        return RedirectResponse("/")
    
    # For users who are logging in for the first time, redirect to Google login
    return await oauth.google.authorize_redirect(request, request.url)

@app.get("/id_token")
async def get_id_token(request: Request):
    """
    Return the ID token and client ID as JSON
    """
    id_token = request.session.get("id_token")
    if not id_token:
        return {"error": "Not authenticated. Please visit '/' to log in first."}
    
    return JSONResponse(content={
        "id_token": id_token,
        "client_id": os.getenv("GOOGLE_CLIENT_ID")
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)
```

---

## Step 7: Run the Application

Start the server with:

```
uvicorn app:app --reload --port 5000
```

---

## Step 8: Test the Application

1. Visit [http://localhost:5000/](http://localhost:5000/) in your browser.
2. You’ll be redirected to Google's login page.
3. Log in with your IITM email account.
4. After successful login, you’ll be redirected back to the application.
5. Visit [http://localhost:5000/id\_token](http://localhost:5000/id_token) to get your ID token and client ID as JSON.

---

## Step 9: Submit the Required Information

Copy the JSON output from the `/id_token` endpoint:

```json
{
  "id_token": "eyJ...",
  "client_id": "YOUR_CLIENT_ID"
}
```

---

## IMPORTANT: Keep the Server Running

**DO NOT stop the FastAPI server until after you have submitted the entire Graded Assignment!**

If you need to restart your computer or close your terminal, simply run the command again:

```
uvicorn app:app --reload --port 5000
```

---

## Troubleshooting

* **redirect\_uri\_mismatch**: Ensure your redirect URI in Google Cloud Console exactly matches `http://localhost:5000/`.
* **Authentication fails**: Verify your `.env` file contains the correct `CLIENT_ID` and `CLIENT_SECRET`.
* **Port 5000 in use**: You can specify a different port by changing the `--port` flag, but update the redirect URI in Google Cloud Console accordingly.
* **Login issues**: Use your IITM email account for login.

---


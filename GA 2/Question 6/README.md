---

# Deploying a FastAPI Student Marks API to Vercel

This guide walks you through building and deploying a simple FastAPI application on **Vercel**. The API serves student marks from a JSON dataset and supports querying by student name.

---

## 🔍 What You'll Build

A web API that:

* Reads student marks from a JSON file
* Accepts names via query parameters
* Returns matching students' marks as JSON
* Enables **CORS** to allow requests from any frontend

---

## 📁 Project Structure

Create a GitHub repository with the following structure:

```
student-vercel-api/
│
├── api/
│   ├── index.py                 # FastAPI app code
│   └── vercel-data.json          # JSON file with student marks
│
├── vercel.json                 # Vercel config file
├── requirements.txt            # Python dependencies
└── README.md                   # Project info (added for steps)
```

---

## ✅ Step-by-Step Instructions

### Step 1: Set Up a GitHub Repository

1. Go to [GitHub](https://github.com/) and create a new repository.
2. Name it something like `student-vercel-api`.
3. Set visibility to **Public**.
4. Initialize it with a README file.

---

### Step 2: Add the API Code

#### `api/index.py`

```python
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json, os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load student data
data_path = os.path.join(os.path.dirname(__file__), "marks-data.json")
with open(data_path) as f:
    students = json.load(f)

@app.get("/api")
async def get_marks(name: List[str] = Query(None)):
    if not name:
        return {"error": "Please provide at least one name"}
    results = [
        next((s["marks"] for s in students if s["name"].lower() == n.lower()), None)
        for n in name
    ]
    return {"marks": results}

@app.get("/")
async def root():
    return {"message": "Use /api?name=Alice&name=Bob to get student marks"}

# Optional: Local testing
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("index:app", host="0.0.0.0", port=8000, reload=True)
```

---

### Step 3: Add Supporting Files

#### `api/vercel-data.json`

Place your student marks dataset here. This should be a list of objects like:

```json
[
  { "name": "Alice", "marks": 88 },
  { "name": "Bob", "marks": 72 }
]
```

#### `vercel.json`

```json
{
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "api/index.py"
    }
  ]
}
```

#### `requirements.txt`

```
fastapi
uvicorn
```

---

## 🧪 Optional: Run the API Locally

1. Install dependencies:

   ```bash
   pip install fastapi uvicorn
   ```

2. Run the API:

   ```bash
   cd api
   uvicorn index:app --reload
   ```

3. Access it at:
   [http://localhost:8000/api?name=Alice\&name=Bob](http://localhost:8000/api?name=Alice&name=Bob)

---

## 🚀 Deploying to Vercel

### Step 1: Sign In to Vercel

* Visit [vercel.com](https://vercel.com/)
* Sign up or log in
* Connect your GitHub account

### Step 2: Import & Deploy

1. Click **New Project** from your Vercel dashboard.
2. Select your GitHub repo.
3. Vercel auto-detects your FastAPI setup via `vercel.json`.
4. Click **Deploy** and wait for the process to complete.

---

## ✅ Test Your API

After deployment, your API will be live at:

```
https://<your-vercel-project>.vercel.app/api?name=Alice
```

Example response:

```json
{
  "marks": [88]
}
```

> If you get an error, wait a few minutes—deployment and caching delays may occur.

---

## 🛠 Troubleshooting & Tips

* The `vercel-data.json` file must be in the `api/` folder.
* Your FastAPI app **must be** in `index.py` for Vercel's build system to detect it.
* If testing locally from the root, use `uvicorn api.index:app --reload`.
* Vercel redeploys automatically on every `git push`.

---


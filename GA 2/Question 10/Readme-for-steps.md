---

# FastAPI Server for Student Data

This guide shows you how to set up a FastAPI server to serve student data from a CSV file with filtering by class.

---

## Step 1: Project Structure

Create the following structure:

```
my-api/
├── q-fastapi.csv     # Student data CSV
├── main.py           # FastAPI app
└── requirements.txt  # Dependencies
```

---

## Step 2: Prepare the CSV File

1. Download the CSV file from the assignment.
2. Rename it to `q-fastapi.csv` and place it in your project directory.

---

## Step 3: Requirements File

Create `requirements.txt` with:

```
fastapi
uvicorn
pandas
```

---

## Step 4: Install Dependencies

Run the following in your terminal:

```
pip install -r requirements.txt
```

---

## Step 5: FastAPI Application

Create `main.py`:

```python
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from typing import List, Optional

app = FastAPI()

# Enable CORS
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["GET"], allow_headers=["*"])

df = pd.read_csv("q-fastapi.csv")

def get_students_data(class_filters=None):
    filtered_df = df[df['class'].isin(class_filters)] if class_filters else df
    return [{"studentId": int(row["studentId"]), "class": row["class"]} for _, row in filtered_df.iterrows()]

@app.get("/api")
async def get_students(class_param: Optional[List[str]] = Query(None, alias="class")):
    return {"students": get_students_data(class_param)}

@app.get("/")
async def root():
    return {"message": "Student API is running. Use /api endpoint to get student data."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
```

---

## Step 6: Run the Server

Start the server with:

```
uvicorn main:app --reload
```

---

## Step 7: Access the API

Your API is now available at `http://127.0.0.1:8000/api`. Examples:

* All students: `http://127.0.0.1:8000/api`
* Class 1A: `http://127.0.0.1:8000/api?class=1A`
* Classes 1A & 1B: `http://127.0.0.1:8000/api?class=1A&class=1B`

---

## Step 8: Submit the URL

Use this URL in your submission:

```
http://127.0.0.1:8000/api
```

---

## IMPORTANT: Keep the Server Running

Do not stop the server until after submitting your assignment. If needed, restart it with:

```
uvicorn main:app --reload
```

---

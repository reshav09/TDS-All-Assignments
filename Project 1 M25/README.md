---

# TDS Virtual TA — 2025 Project

A Retrieval-Augmented Generation (RAG) API powered by OpenAI and FAISS for answering student questions on TDS course content.

## 💻 Features

* Uses scraped TDS content + Discourse posts
* RAG-based question answering
* Deployable on Railway or Render (Dockerized)

## 🧱 Project Structure

```
app/
├── data/                  # Precomputed embeddings + metadata
├── discourse_raw_json/   # Optional raw data
├── embed.py
├── rag.py
└── index.py
Dockerfile
requirements.txt
```

## ⚙ Environment Variables

* `AIPROXY_TOKEN` — Your OpenAI proxy token.

**Important:**
Do **not** upload or push your `.env` file to version control. Instead, manually add the environment variables in the dashboard settings of [Render](https://render.com) or [Railway](https://railway.app) during deployment.

## 🚀 Deployment

### 🚂 Railway

1. Create a Railway account.
2. Connect your GitHub repository.
3. Railway auto-detects the `Dockerfile`.
4. Add required environment variables in project settings.
5. Deploy.

### 🛰️ Render

1. Create a Render account.
2. Connect your GitHub repository.
3. Choose Docker as the deployment method.
4. Manually add environment variables in the dashboard.
5. Deploy.

> ⚠️ Make sure CORS is enabled to allow requests from your frontend if you're testing locally or using a separate domain.

## 🧪 API Usage

### Health Check

```http
GET https://your-url/
```

### Ask a Question (GET)

```http
GET https://your-url/api?q=what%20is%20CNN
```

### Ask a Question (POST)

```http
POST https://your-url/api
Content-Type: application/json

{
  "question": "What is CNN?"
}
```

## 🔑 Author

Reshav Sharma
2025 TDS Project

---

## 📝 Notes

* This codebase is a **reference implementation** to demonstrate the approach used.
* You will need to modify it to suit your specific dataset and use case.
* It works best once you have scraped your course content in JSON format.
* Scraping itself is straightforward—feel free to customize the scraping script to match your data structure.
* Suggestions are welcome!

---

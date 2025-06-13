
from flask import Flask, request, jsonify
from flask_cors import CORS
from rag import answer_question
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)
load_dotenv()

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"message": "TDS Virtual TA API is running!"})

@app.route("/api", methods=["GET", "POST"])
def api():
    if request.method == "POST":
        data = request.get_json()
        question = data.get("question")
    elif request.method == "GET":
        question = request.args.get("q")
    
    if not question:
        return jsonify({"error": "Question is required."}), 400

    answer, links = answer_question(question)
    return jsonify({"answer": answer, "links": links})

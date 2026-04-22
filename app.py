from flask import Flask, request, jsonify
from rag import retrieve
from llm import generate_answer

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")
    chunks = retrieve(question)
    answer = generate_answer(chunks, question)
    return jsonify({"question": question, "answer": answer, "sources": chunks})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
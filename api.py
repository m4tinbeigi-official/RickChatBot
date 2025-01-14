from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
chatbot = pipeline("text-generation", model="gpt2")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = chatbot(user_input, max_length=50)[0]['generated_text']
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
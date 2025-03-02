from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

OLLAMA_URL = "http://localhost:11434/api/generate"  # Ollama's local API endpoint

# Custom MyOptic AI Knowledge Base
MYOPTIC_CONTEXT = """
MyOptic AI is an AI-driven healthcare assistant focused on eye health. 
It helps users by analyzing retinal scans, tracking eyesight changes, 
and predicting risks of myopia, glaucoma, and retinal detachment. 
It provides users with insights on eye care, lens usage, and vision correction. 
It's owned and run by Yuvika Gupta, Mahi Tyagi, Rishika Singh, and Manan Singh.
"""

@app.route("/")
def home():
    return "Flask Server is Running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": "llama3",  # Change this to "llama3" if needed
            "prompt": f"{MYOPTIC_CONTEXT}\nUser: {user_message}\nAI:",
            "stream": False,
            "options": {
                "num_predict": 30,  # Limits response length (Lower = Faster)
                "temperature": 0.2  # Lower values = More structured & faster responses
            }
        })

        response_data = response.json()
        bot_reply = response_data["response"]

        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

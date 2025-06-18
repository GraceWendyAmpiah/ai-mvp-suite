from flask import Blueprint, request, jsonify
import nltk
import os

# Download punkt tokenizer if not already downloaded
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")
try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab")

# Define intents and functions directly (avoiding pickle issues)
intents = {
    "ride_request": [
        "ride to", "need a ride", "going to", "travel to", "going from",
        "heading to", "take me to", "go to", "pick me up", "can you take me to"
    ],
    "delivery_request": [
        "deliver", "send to", "ship to", "send package", "drop off",
        "take it to", "deliver to", "send item", "drop off package", "take the package"
    ],
    "help_request": [
        "help", "what can i do", "how to use", "instructions", "guide", "how does this work",
        "can you help me", "what is KADA", "how do I request a ride", "how to book a delivery"
    ]
}

def process_message(message):
    tokens = nltk.word_tokenize(message.lower())
    if "help" in tokens or "how" in tokens:
        return "help_request"
    for intent, keywords in intents.items():
        for keyword in keywords:
            if all(word in tokens for word in keyword.split()):
                return intent
    return "unknown"

def generate_response(intent):
    if intent == "ride_request":
        return "Your ride has been booked. Please wait for your driver."
    elif intent == "delivery_request":
        return "Your delivery order has been booked. Please await the dispatch rider."
    elif intent == "help_request":
        return "To request a ride, type 'Ride to [destination]'. To send a package, type 'Send to [destination]'."
    elif intent == "unknown":
        return "Sorry, I didn't understand that. Try saying 'I need a ride' or 'Send a package to [destination]'. Type 'Help' for more assistance."

kada_bp = Blueprint("kada", __name__)

@kada_bp.route("/process", methods=["POST"])
def process_kada_sms():
    data = request.get_json()
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"error": "No message provided"}), 400

    intent = process_message(message)
    response = generate_response(intent)

    return jsonify({
        "message": message,
        "intent": intent,
        "response": response
    })


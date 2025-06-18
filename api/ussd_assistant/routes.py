from flask import Blueprint, request, jsonify
from models.asad_nlp.asad_intent import classify_intent
from api.ussd_assistant.logic.core import handle_intent

# Blueprint for ASAD endpoints
ussd_assistant_bp = Blueprint("ussd_assistant", __name__)

# NLP injection route, matches POST to /asad/nlp-inject
@ussd_assistant_bp.route("/nlp-inject", methods=["POST"])
def nlp_inject():
    data = request.get_json()
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Step 1: Use NLP model to classify the user's intent
    intent_result = classify_intent(user_input)

    # Step 2: Handle the recognized intent and generate USSD-like response
    logic_result = handle_intent(intent_result["intent"], user_input)

    return jsonify({
        "intent": intent_result["intent"],
        "score": round(intent_result["score"], 3),
        "action_result": logic_result,
        "full_probs": intent_result["full_probs"]
    })

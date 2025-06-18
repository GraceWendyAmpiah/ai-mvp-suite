from flask import Blueprint, request, jsonify
from models.sms_guard.fraud_keywords import is_suspicious_sms

sms_guard_bp = Blueprint('sms_guard', __name__)

@sms_guard_bp.route('/check', methods=['POST'])
def sms_guard_check():
    data = request.get_json()
    message = data.get("message", "")
    
    print("\n=== DEBUG: Received SMS ===")
    print(message)

    result = is_suspicious_sms(message)

    print("=== DEBUG: Classification Result ===")
    print(result)

    return jsonify({"result": result})

from models.sms_guard.fraud_keywords import is_suspicious_sms

def classify_message(sms_text: str) -> dict:
    """
    Classify the given SMS message as either 'fraud' or 'legit'.

    Args:
        sms_text (str): The SMS message content.

    Returns:
        dict: Classification result with original text and label.
    """
    if not sms_text.strip():
        return {
            "error": "Empty message received"
        }

    is_fraud = is_suspicious_sms(sms_text)

    return {
        "message": sms_text,
        "classification": "fraud" if is_fraud else "legit"
    }

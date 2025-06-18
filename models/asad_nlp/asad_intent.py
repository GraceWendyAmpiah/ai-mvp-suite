# Simple rule-based intent classifier as fallback
import re
import os

def classify_intent(text):
    """
    Simple rule-based intent classification for ASAD
    Returns intent classification similar to the BERT model format
    """
    text = text.lower().strip()
    
    # Define intent patterns
    patterns = {
        "send_money": [
            r"send.*money", r"transfer.*money", r"send.*cedis", r"transfer.*cedis",
            r"send.*\d+", r"transfer.*\d+", r"pay.*\d+", r"give.*money"
        ],
        "check_balance": [
            r"check.*balance", r"balance.*check", r"my.*balance", r"account.*balance",
            r"how.*much.*money", r"what.*balance"
        ],
        "buy_airtime": [
            r"buy.*airtime", r"purchase.*airtime", r"top.*up", r"recharge",
            r"credit.*phone", r"load.*airtime"
        ],
        "pay_bills": [
            r"pay.*bill", r"pay.*electricity", r"pay.*water", r"pay.*utility",
            r"bill.*payment", r"utility.*payment"
        ],
        "allow_cashout": [
            r"allow.*cashout", r"enable.*cashout", r"permit.*cashout",
            r"authorize.*withdrawal", r"approve.*cashout"
        ]
    }
    
    # Check patterns and calculate confidence
    for intent, pattern_list in patterns.items():
        for pattern in pattern_list:
            if re.search(pattern, text):
                # Simple confidence based on pattern match strength
                confidence = 0.85 if len(re.findall(pattern, text)) > 0 else 0.7
                
                return {
                    "intent": intent,
                    "score": confidence,
                    "full_probs": {
                        intent: confidence,
                        "unknown": 1 - confidence
                    }
                }
    
    # Default to unknown intent
    return {
        "intent": "unknown",
        "score": 0.5,
        "full_probs": {
            "unknown": 0.5,
            "send_money": 0.1,
            "check_balance": 0.1,
            "buy_airtime": 0.1,
            "pay_bills": 0.1,
            "allow_cashout": 0.1
        }
    }

# === Test Run ===
if __name__ == "__main__":
    test_input = "send 10 cedis to my sister on MTN"
    result = classify_intent(test_input)
    print("Predicted Intent:", result["intent"])
    print("Confidence Score:", result["score"])
    print("All Probabilities:", result["full_probs"])


import re

def is_suspicious_sms(sms_text):
    print("\n--- Analyzing SMS ---")
    print("Original:", repr(sms_text))

    sms_text = sms_text.lower()
    sms_text = re.sub(r'\s+', ' ', sms_text)  # Normalize whitespace
    sms_text = sms_text.replace('\xa0', ' ')
    sms_text = sms_text.strip()

    print("Normalized:", repr(sms_text))

    # Legitimate SMS footers (not always present)
    legit_footer_phrases = [
        "download the mtn momo app",
        "transact safely with the mtn app",
        "thank you for using"
    ]
    for footer in legit_footer_phrases:
        if footer in sms_text:
            print("Matched footer:", footer)
            return "legit"

    # Updated legit message patterns with optional colons
    legit_patterns = [
        r"payment received for .*? from .*? current balance[:]?\s*ghs .*? transaction id[:]?\s*\d+",
        r"you have received .*? current balance[:]?\s*ghs .*? transaction id[:]?\s*\d+",
        r"cash out of .*? successful .*? transaction id[:]?\s*\d+",
        r"you paid .*? to .*? transaction id[:]?\s*\d+"
    ]
    for pattern in legit_patterns:
        if re.search(pattern, sms_text):
            print("Matched legit pattern:", pattern)
            return "legit"

    # Fraud signal patterns (bad structure or grammar)
    suspicious_signs = [
        r"current balance ghs[^0-9]",             # balance has no amount
        r"available balance ghs[^0-9]",           # same
        r"fee charged[:]? ghs 0[^0-9]",           # bad formatting
        r"cash in received for .*? from",         # unusual phrasing
        r"you have been sent",                    # informal
        r"pending transaction"                    # odd transaction status
    ]
    for pattern in suspicious_signs:
        if re.search(pattern, sms_text):
            print("Matched suspicious pattern:", pattern)
            return "fraud"

    print("No patterns matched. Returning unknown.")
    return "unknown"

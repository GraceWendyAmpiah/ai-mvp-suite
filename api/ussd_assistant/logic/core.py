from .send_money import handle as handle_send_money
from .buy_airtime import handle as handle_buy_airtime
from .pay_bills import handle as handle_pay_bills
from .check_balance import handle as handle_check_balance
from .allow_cashout import handle as handle_allow_cash_out

def handle_ussd_input(history, user_input):
    """
    Traditional USSD navigation (button-based). 
    Routes based on user's navigation state.
    """
    if not history or history[-1] == "main_menu":
        if user_input == "1":
            history.append("1")
            return handle_send_money(history, user_input)
        elif user_input == "2":
            history.append("2")
            return handle_buy_airtime(history, user_input)
        elif user_input == "3":
            history.append("3")
            return handle_pay_bills(history, user_input)
        elif user_input == "4":
            history.append("4")
            return handle_check_balance(history, user_input)
        elif user_input == "5":
            history.append("5")
            return handle_allow_cash_out(history, user_input)
        else:
            return "Invalid option. Please try again."

    # Handle continuation based on history
    if history[0] == "1":
        return handle_send_money(history, user_input)
    elif history[0] == "2":
        return handle_buy_airtime(history, user_input)
    elif history[0] == "3":
        return handle_pay_bills(history, user_input)
    elif history[0] == "4":
        return handle_check_balance(history, user_input)
    elif history[0] == "5":
        return handle_allow_cash_out(history, user_input)

    return "Session ended or navigation logic not implemented."


# === NLP-Based Intent Handler ===

def handle_intent(intent_label, user_input):
    """
    Given an intent label (e.g. 'send_money'), route to the appropriate handler directly.
    This simulates starting from a recognized user intent without full step-by-step history.
    """
    history = ["main_menu"]

    if intent_label == "send_money":
        history.append("1")
        return handle_send_money(history, user_input)

    elif intent_label == "buy_airtime":
        history.append("2")
        return handle_buy_airtime(history, user_input)

    elif intent_label == "pay_bill":
        history.append("3")
        return handle_pay_bills(history, user_input)

    elif intent_label == "check_balance":
        history.append("4")
        return handle_check_balance(history, user_input)

    elif intent_label == "allow_cash_out":
        history.append("5")
        return handle_allow_cash_out(history, user_input)

    else:
        return f"❌ No handler found for intent: {intent_label}"

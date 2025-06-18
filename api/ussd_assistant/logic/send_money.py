# send_money.py

def handle(history, user_input):
    step = len(history)

    if step == 2:
        # Step 1: Choose recipient type
        response = (
            "Send Money:\n"
            "1. To MTN MoMo user\n"
            "2. To other networks\n"
            "3. To Ezwich\n"
            "4. To Bank Account"
        )
        return response

    elif step == 3:
        if user_input == "1":
            history.append("send_money_mtn")
            return "Enter recipient's MoMo number:"
        elif user_input == "2":
            history.append("send_money_other_networks")
            return "Enter recipient's number:"
        elif user_input == "3":
            history.append("send_money_ezwich")
            return "Enter recipient's Ezwich number:"
        elif user_input == "4":
            history.append("send_money_bank")
            return "Enter bank account number:"
        else:
            return "Invalid option. Try again."

    elif step == 4:
        history.append(user_input)
        return "Enter amount to send:"

    elif step == 5:
        history.append(user_input)
        return "Enter reference (or leave blank):"

    elif step == 6:
        history.append(user_input)
        recipient = history[3]
        amount = history[4]
        reference = history[5] or "No reference"
        return (
            f"You're sending GHS {amount} to {recipient}.\n"
            f"Reference: {reference}\n"
            "Type 'confirm' to proceed or 'cancel' to stop."
        )

    elif step == 7:
        if user_input.lower() == "confirm":
            history.append("confirmed")
            return "Enter your MoMo PIN:"
        elif user_input.lower() == "cancel":
            return "Transaction cancelled."
        else:
            return "Please type 'confirm' or 'cancel'."

    elif step == 8:
        pin = user_input
        amount = history[4]
        recipient = history[3]
        return f"✅ GHS {amount} sent to {recipient}. Thank you for using MoMo."

    return "Sorry, something went wrong in the Send Money flow."

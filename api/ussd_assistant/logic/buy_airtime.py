# buy_airtime.py

def handle(history, user_input):
    step = len(history)

    if step == 2:
        response = (
            "Airtime & Bundles:\n"
            "1. Buy Airtime\n"
            "2. Buy Data Bundle"
        )
        return response

    elif step == 3:
        if user_input == "1":
            history.append("buy_airtime_self")
            return "Enter amount to buy for yourself:"
        elif user_input == "2":
            history.append("buy_data")
            return "Enter data bundle amount (e.g., 5 for 5 cedis):"
        else:
            return "Invalid option. Try again."

    elif step == 4:
        history.append(user_input)
        amount = user_input
        return (
            f"You're about to buy GHS {amount} of airtime/data for yourself.\n"
            "Type 'confirm' to proceed or 'cancel' to stop."
        )

    elif step == 5:
        if user_input.lower() == "confirm":
            history.append("confirmed")
            amount = history[4]
            return f"✅ You have successfully bought GHS {amount} airtime/data."
        elif user_input.lower() == "cancel":
            return "Transaction cancelled."
        else:
            return "Please type 'confirm' or 'cancel'."

    return "Sorry, something went wrong in the Buy Airtime flow."

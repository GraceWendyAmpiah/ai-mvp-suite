# pay_bills.py

def handle(history, user_input):
    step = len(history)

    if step == 2:
        return (
            "MoMoPay & Pay Bill:\n"
            "1. Pay Bill\n"
            "2. MoMoPay"
        )

    elif step == 3:
        if user_input == "1":
            history.append("pay_bill")
            return (
                "Select Bill Type:\n"
                "1. Electricity\n"
                "2. Water\n"
                "3. TV Subscription"
            )
        elif user_input == "2":
            history.append("momopay")
            return "Enter merchant ID:"
        else:
            return "Invalid option. Try again."

    elif step == 4:
        history.append(user_input)
        if history[2] == "pay_bill":
            return "Enter customer account number:"
        elif history[2] == "momopay":
            return "Enter amount to pay:"

    elif step == 5:
        history.append(user_input)
        return "Enter amount:"

    elif step == 6:
        history.append(user_input)
        return (
            f"You are about to pay GHS {history[-1]}.\n"
            "Type 'confirm' to proceed or 'cancel' to stop."
        )

    elif step == 7:
        if user_input.lower() == "confirm":
            history.append("confirmed")
            return "✅ Payment successful. Thank you."
        elif user_input.lower() == "cancel":
            return "Transaction cancelled."
        else:
            return "Please type 'confirm' or 'cancel'."

    return "Something went wrong in the Pay Bills flow."

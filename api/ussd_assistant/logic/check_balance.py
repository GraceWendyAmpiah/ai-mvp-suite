# check_balance.py

def handle(history, user_input):
    step = len(history)

    if step == 2:
        return (
            "Check Balance:\n"
            "1. MoMo Balance\n"
            "2. Airtime Balance\n"
            "3. Data Balance"
        )

    elif step == 3:
        history.append(user_input)
        if user_input == "1":
            return "Your MoMo balance is GHS 132.45"
        elif user_input == "2":
            return "You have GHS 5.30 airtime remaining"
        elif user_input == "3":
            return "You have 1.2 GB data left"
        else:
            return "Invalid option. Try again."

    return "Sorry, could not complete the balance check."

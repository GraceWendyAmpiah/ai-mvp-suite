# allow_cash_out.py

def handle(history, user_input):
    step = len(history)

    if step == 2:
        return (
            "Allow Cash Out:\n"
            "1. Yes\n"
            "2. No"
        )

    elif step == 3:
        history.append(user_input)
        if user_input == "1":
            return "✅ Cash Out Enabled."
        elif user_input == "2":
            return "❌ Cash Out Disabled."
        else:
            return "Invalid option. Please choose 1 (Yes) or 2 (No)."

    return "Something went wrong in the Allow Cash Out flow."

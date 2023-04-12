import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "help":
        return "`Possible commands: 'hello', 'roll'`"
    if p_message == "roll":
        return random.randint(1,6)
    if p_message == "hello":
        return "Hey There!"
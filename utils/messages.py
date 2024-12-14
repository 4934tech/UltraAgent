# utils/messages.py
def get_system_message():
    return {
        "role": "system",
        "content": (
            "You are a home automation AI assistant. List devices and control lights by user requests."
        )
    }

def get_developer_message():
    return {
        "role": "assistant",
        "content": (
            "Ensure you list devices before controlling them. Confirm actions to the user."
        )
    }

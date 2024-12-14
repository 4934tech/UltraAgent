if __name__ == "__main__":
    from config.env import OPENAI_API_KEY, GOVEE_API_KEY
    from api.openai_client import create_openai_client
    from conversation.conversation_runner import run_conversation

    client = create_openai_client(OPENAI_API_KEY)
    user_input = "Can you turn on the kitchen light?"
    print(run_conversation(user_input, client, GOVEE_API_KEY))

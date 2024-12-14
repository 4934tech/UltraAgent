from conversation.conversation_runner import run_interactive_conversation

if __name__ == "__main__":
    from config.env import OPENAI_API_KEY, GOVEE_API_KEY
    from api.openai_client import create_openai_client

    client = create_openai_client(OPENAI_API_KEY)
    run_interactive_conversation(client, GOVEE_API_KEY)

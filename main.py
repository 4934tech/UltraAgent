from audio.recognizer import recognize_speech
from audio.elevenlabs_tts import speak_with_elevenlabs
from conversation.conversation_runner import run_conversation
from config.env import OPENAI_API_KEY, GOVEE_API_KEY, ELEVENLABS_API_KEY
from api.openai_client import create_openai_client

def run_voice_conversation():
    """Run an interactive voice conversation."""
    client = create_openai_client(OPENAI_API_KEY)
    print("Voice assistant initialized. Say 'exit' to end the session.")
    speak_with_elevenlabs(ELEVENLABS_API_KEY, "Hello, how can I assist you with your Govee devices?")

    # Initialize the chat history
    messages = []

    while True:
        # Get voice input
        user_message = recognize_speech()
        if not user_message:
            continue

        print(f"You: {user_message}")
        if user_message.lower() == "exit":
            speak_with_elevenlabs(ELEVENLABS_API_KEY, "Goodbye!")
            break

        # Process conversation
        response = run_conversation(user_message, client, GOVEE_API_KEY, messages)

        # Speak and display the assistant's response
        print(f"Assistant: {response}")
        speak_with_elevenlabs(ELEVENLABS_API_KEY, response)

if __name__ == "__main__":
    run_voice_conversation()

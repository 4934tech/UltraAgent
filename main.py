from audio.recognizer import recognize_speech
from audio.elevenlabs_tts import speak_with_elevenlabs
from conversation.conversation_runner import run_conversation
from config.env import OPENAI_API_KEY, GOVEE_API_KEY, ELEVENLABS_API_KEY
from api.openai_client import create_openai_client
from audio.tts_controller import play_tts_with_interruption

def run_voice_conversation():
    client = create_openai_client(OPENAI_API_KEY)
    print("Voice assistant initialized. Say 'exit' to end the session.")
    speak_with_elevenlabs(ELEVENLABS_API_KEY, "Phoenix listening in.", "Phoenix")
    messages = []

    while True:
        user_message = recognize_speech()
        if not user_message:
            continue
        print(f"You: {user_message}")
        if user_message.lower() == "exit":
            speak_with_elevenlabs(ELEVENLABS_API_KEY, "Phoenix out.", "Phoenix")
            break
        response = run_conversation(user_message, client, GOVEE_API_KEY, messages)
        print(f"Assistant: {response}")

        interruption = play_tts_with_interruption(ELEVENLABS_API_KEY, response, "Phoenix")

        while interruption:
            print(f"You (interruption): {interruption}")
            response = run_conversation(interruption, client, GOVEE_API_KEY, messages)
            print(f"Assistant: {response}")
            interruption = play_tts_with_interruption(ELEVENLABS_API_KEY, response, "Phoenix")

if __name__ == "__main__":
    run_voice_conversation()

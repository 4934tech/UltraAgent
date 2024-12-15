"""
    UltraAgent is an AI agent with real-world powers to control many applications.
    Copyright (C) 2024  Olav Sharma - 4934.tech

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from audio.recognizer import recognize_speech
from audio.elevenlabs_tts import speak_with_elevenlabs
from conversation.conversation_runner import run_conversation
from config.env import OPENAI_API_KEY, GOVEE_API_KEY, ELEVENLABS_API_KEY
from api.openai_client import create_openai_client
from audio.tts_controller import play_tts_with_interruption

print("UltraAgent  Copyright (C) 2024  Olav Sharma - 4934.tech\nThis program comes with ABSOLUTELY NO WARRANTY.\nThis is free software, and you are welcome to redistribute it\nunder certain conditions. To learn more, go to: <https://github.com/4934tech/UltraAgent/blob/master/license.md> for details.")

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

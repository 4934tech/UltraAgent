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

import multiprocessing
from src.audio.recognizer import recognize_speech
from src.audio.elevenlabs_tts import speak_with_elevenlabs

def play_tts_with_interruption(api_key, text, voice):
    """
    Play TTS using speak_with_elevenlabs in a separate process.
    While it's speaking, continuously listen for user speech.
    If user speaks, terminate the TTS process and return that new user message.
    If TTS finishes with no interruption, return None.
    """
    tts_process = multiprocessing.Process(
        target=speak_with_elevenlabs,
        args=(api_key, text, voice),
        daemon=True
    )
    tts_process.start()

    # Continuously check for user speech while TTS is playing
    while tts_process.is_alive():
        interrupt_message = recognize_speech()
        if interrupt_message and interrupt_message.lower() != "no audio inputted by user.":
            # User interrupted mid-speech
            tts_process.terminate()
            tts_process.join()
            return interrupt_message

    # TTS finished with no interruption
    tts_process.join()
    return None

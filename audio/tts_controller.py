# audio/tts_controller.py
import multiprocessing
from audio.recognizer import recognize_speech
from audio.elevenlabs_tts import speak_with_elevenlabs

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

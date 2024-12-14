from elevenlabs.client import ElevenLabs
from elevenlabs import stream

def speak_with_elevenlabs(api_key, text, voice="Phoenix"):
    """
    Use ElevenLabs TTS to speak the given text via streaming.

    :param api_key: Your ElevenLabs API key.
    :param text: Text to convert to speech.
    :param voice: The ElevenLabs voice to use.
    """
    try:
        # Initialize ElevenLabs client
        client = ElevenLabs(api_key=api_key)

        # Generate the audio stream
        audio_stream = client.generate(
            text=text,
            voice=voice,
            stream=True
        )

        # Stream and play the audio
        stream(audio_stream)
    except Exception as e:
        print(f"Error during ElevenLabs TTS streaming: {e}")

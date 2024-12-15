# audio/elevenlabs_tts.py
from elevenlabs.client import ElevenLabs
from elevenlabs import stream, VoiceSettings

def speak_with_elevenlabs(api_key, text, voice):
    """
    Use ElevenLabs TTS to speak the given text via streaming.
    """
    try:
        # Initialize ElevenLabs client
        client = ElevenLabs(api_key=api_key)

        voice_settings = VoiceSettings(
            stability=0.5,
            similarity_boost=0.8
        )

        # Generate the audio stream
        audio_stream = client.generate(
            text=text,
            voice=voice,
            voice_settings=voice_settings,
            stream=True,
            model="eleven_turbo_v2_5",
            optimize_streaming_latency=3
        )

        # Stream and play the audio
        stream(audio_stream)
    except Exception as e:
        print(f"Error during ElevenLabs TTS streaming: {e}")

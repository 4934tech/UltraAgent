"""
    UltraAgent is an AI agent with real-world powers to control many applications.
    Copyright (C) 2024  Olav "Olavorw" Sharma - 4934 Tech

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

from elevenlabs.client import ElevenLabs
from elevenlabs import stream, VoiceSettings

def speak_with_elevenlabs(api_key, text, voice):
    """
    Use ElevenLabs TTS to speak the given text via streaming.
    """
    try:
        
        client = ElevenLabs(api_key=api_key)

        voice_settings = VoiceSettings(
            stability=0.5,
            similarity_boost=0.8
        )

        
        audio_stream = client.generate(
            text=text,
            voice=voice,
            voice_settings=voice_settings,
            stream=True,
            model="eleven_turbo_v2_5",
            optimize_streaming_latency=3
        )

        
        stream(audio_stream)
    except Exception as e:
        print(f"Error during ElevenLabs TTS streaming: {e}")

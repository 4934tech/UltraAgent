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

import requests
import io
import sounddevice as sd
import numpy as np
from pydub import AudioSegment
from pydub.playback import play

def speak_with_elevenlabs(api_key, text, voice_name):
    """
    Use ElevenLabs TTS to speak the given text using the REST API directly.
    """
    try:
        # API endpoint
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_name}"
        
        # Request headers
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": api_key
        }
        
        # Request body
        body = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75
            }
        }
        
        # Make the API request
        response = requests.post(url, json=body, headers=headers)
        
        if response.status_code != 200:
            raise Exception(f"API request failed with status {response.status_code}: {response.text}")
        
        # Convert response content to audio
        audio = AudioSegment.from_mp3(io.BytesIO(response.content))
        
        # Play the audio
        play(audio)
        
    except Exception as e:
        error_msg = str(e)
        print(f"Error during ElevenLabs TTS: {error_msg}")
        
        if "Could not find voice" in error_msg:
            print("Voice not found. Please check the voice name and try again.")
        elif "Invalid API key" in error_msg or "Unauthorized" in error_msg:
            print("Invalid API key. Please check your ElevenLabs API key.")
        elif "quota" in error_msg.lower():
            print("API quota exceeded. Please check your ElevenLabs subscription.")
        elif "WinError" in error_msg:
            print("Audio device not found. Please check your audio settings and ensure speakers/headphones are connected.")

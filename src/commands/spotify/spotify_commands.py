"""
Spotify control commands for UltraAgent
"""

from typing import Dict, Any, List
from src.commands.base_command import BaseCommand
from src.api.spotify_client import (
    spotify_get_playback,
    spotify_get_current_track,
    spotify_play,
    spotify_pause,
    spotify_next_track,
    spotify_previous_track,
    spotify_set_volume
)

class SpotifyDebugCommand(BaseCommand):
    @property
    def name(self) -> str:
        return "spotify_debug"

    @property
    def description(self) -> str:
        return "Debug Spotify configuration and connection"

    @property
    def schema(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }

    @property
    def required_api_keys(self) -> List[str]:
        return ["SPOTIFY_CLIENT_ID", "SPOTIFY_CLIENT_SECRET", "SPOTIFY_REDIRECT_URI"]

    def execute(self, **kwargs) -> Dict[str, Any]:
        client_id = kwargs.pop("SPOTIFY_CLIENT_ID")
        client_secret = kwargs.pop("SPOTIFY_CLIENT_SECRET")
        redirect_uri = kwargs.pop("SPOTIFY_REDIRECT_URI")
        return spotify_get_current_track(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri
        )

class SpotifyPlayCommand(BaseCommand):
    @property
    def name(self) -> str:
        return "spotify_play"

    @property
    def description(self) -> str:
        return "Resume Spotify playback"

    @property
    def schema(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }

    @property
    def required_api_keys(self) -> List[str]:
        return ["SPOTIFY_CLIENT_ID", "SPOTIFY_CLIENT_SECRET", "SPOTIFY_REDIRECT_URI"]

    def execute(self, **kwargs) -> Dict[str, Any]:
        client_id = kwargs.get("SPOTIFY_CLIENT_ID")
        client_secret = kwargs.get("SPOTIFY_CLIENT_SECRET")
        redirect_uri = kwargs.get("SPOTIFY_REDIRECT_URI")
        
        if not all([client_id, client_secret, redirect_uri]):
            return {"status": "error", "message": "Missing Spotify credentials"}
        
        return spotify_play(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri
        )

class SpotifyPauseCommand(BaseCommand):
    @property
    def name(self) -> str:
        return "spotify_pause"

    @property
    def description(self) -> str:
        return "Pause Spotify playback"

    @property
    def schema(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }

    @property
    def required_api_keys(self) -> List[str]:
        return ["SPOTIFY_CLIENT_ID", "SPOTIFY_CLIENT_SECRET", "SPOTIFY_REDIRECT_URI"]

    def execute(self, **kwargs) -> Dict[str, Any]:
        client_id = kwargs.pop("SPOTIFY_CLIENT_ID")
        client_secret = kwargs.pop("SPOTIFY_CLIENT_SECRET")
        redirect_uri = kwargs.pop("SPOTIFY_REDIRECT_URI")
        return spotify_pause(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri
        )

class SpotifyNextTrackCommand(BaseCommand):
    @property
    def name(self) -> str:
        return "spotify_next"

    @property
    def description(self) -> str:
        return "Skip to next track on Spotify"

    @property
    def schema(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }

    @property
    def required_api_keys(self) -> List[str]:
        return ["SPOTIFY_CLIENT_ID", "SPOTIFY_CLIENT_SECRET", "SPOTIFY_REDIRECT_URI"]

    def execute(self, **kwargs) -> Dict[str, Any]:
        client_id = kwargs.pop("SPOTIFY_CLIENT_ID")
        client_secret = kwargs.pop("SPOTIFY_CLIENT_SECRET")
        redirect_uri = kwargs.pop("SPOTIFY_REDIRECT_URI")
        return spotify_next_track(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri
        )

class SpotifyPreviousTrackCommand(BaseCommand):
    @property
    def name(self) -> str:
        return "spotify_previous"

    @property
    def description(self) -> str:
        return "Go back to previous track on Spotify"

    @property
    def schema(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }

    @property
    def required_api_keys(self) -> List[str]:
        return ["SPOTIFY_CLIENT_ID", "SPOTIFY_CLIENT_SECRET", "SPOTIFY_REDIRECT_URI"]

    def execute(self, **kwargs) -> Dict[str, Any]:
        client_id = kwargs.pop("SPOTIFY_CLIENT_ID")
        client_secret = kwargs.pop("SPOTIFY_CLIENT_SECRET")
        redirect_uri = kwargs.pop("SPOTIFY_REDIRECT_URI")
        return spotify_previous_track(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri
        )

class SpotifySetVolumeCommand(BaseCommand):
    @property
    def name(self) -> str:
        return "spotify_volume"

    @property
    def description(self) -> str:
        return "Set Spotify playback volume (0-100)"

    @property
    def schema(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {
                    "volume": {
                        "type": "integer",
                        "description": "Volume level (0-100)",
                        "minimum": 0,
                        "maximum": 100
                    }
                },
                "required": ["volume"]
            }
        }

    @property
    def required_api_keys(self) -> List[str]:
        return ["SPOTIFY_CLIENT_ID", "SPOTIFY_CLIENT_SECRET", "SPOTIFY_REDIRECT_URI"]

    def execute(self, **kwargs) -> Dict[str, Any]:
        client_id = kwargs.pop("SPOTIFY_CLIENT_ID")
        client_secret = kwargs.pop("SPOTIFY_CLIENT_SECRET")
        redirect_uri = kwargs.pop("SPOTIFY_REDIRECT_URI")
        volume = kwargs.pop("volume")
        return spotify_set_volume(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            volume=volume
        )

class SpotifyGetCurrentTrackCommand(BaseCommand):
    @property
    def name(self) -> str:
        return "spotify_current"

    @property
    def description(self) -> str:
        return "Get information about the currently playing track"

    @property
    def schema(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }

    @property
    def required_api_keys(self) -> List[str]:
        return ["SPOTIFY_CLIENT_ID", "SPOTIFY_CLIENT_SECRET", "SPOTIFY_REDIRECT_URI"]

    def execute(self, **kwargs) -> Dict[str, Any]:
        client_id = kwargs.pop("SPOTIFY_CLIENT_ID")
        client_secret = kwargs.pop("SPOTIFY_CLIENT_SECRET")
        redirect_uri = kwargs.pop("SPOTIFY_REDIRECT_URI")
        return spotify_get_current_track(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri
        )

def register_commands():
    """Register all Spotify commands"""
    return [
        SpotifyDebugCommand(),
        SpotifyPlayCommand(),
        SpotifyPauseCommand(),
        SpotifyNextTrackCommand(),
        SpotifyPreviousTrackCommand(),
        SpotifySetVolumeCommand(),
        SpotifyGetCurrentTrackCommand()
    ] 
"""
Spotify API client for UltraAgent
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from typing import Dict, Any

def create_spotify_auth(client_id: str, client_secret: str, redirect_uri: str) -> spotipy.Spotify:
    """Create a Spotify client with authentication"""
    scope = "user-read-playback-state user-modify-playback-state user-read-currently-playing playlist-read-private"
    auth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope,
        open_browser=True
    )
    return spotipy.Spotify(auth_manager=auth_manager)

def spotify_get_playback(client_id: str, client_secret: str, redirect_uri: str) -> Dict[str, Any]:
    """Get current playback state"""
    try:
        client = create_spotify_auth(client_id, client_secret, redirect_uri)
        playback = client.current_playback()
        if not playback:
            return {"status": "error", "message": "No active playback found"}
        return {"status": "success", "playback": playback}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def spotify_get_current_track(client_id: str, client_secret: str, redirect_uri: str) -> Dict[str, Any]:
    """Get current track information"""
    try:
        client = create_spotify_auth(client_id, client_secret, redirect_uri)
        playback = client.current_playback()
        if not playback or not playback.get('item'):
            return {"status": "error", "message": "No track currently playing"}
        
        track = playback['item']
        artists = ", ".join([artist['name'] for artist in track['artists']])
        
        track_info = {
            "track_name": track['name'],
            "artists": artists,
            "album": track['album']['name'],
            "is_playing": playback['is_playing'],
            "volume": playback['device']['volume_percent'],
            "device_name": playback['device']['name'],
            "duration_ms": track['duration_ms'],
            "progress_ms": playback['progress_ms']
        }

        progress_sec = round(track_info['progress_ms'] / 1000)
        duration_sec = round(track_info['duration_ms'] / 1000)
        
        return {
            "status": "success",
            "message": (
                f"Now playing: {track_info['track_name']} by {track_info['artists']}\n"
                f"Album: {track_info['album']}\n"
                f"Progress: {progress_sec}s / {duration_sec}s\n"
                f"Volume: {track_info['volume']}%\n"
                f"Device: {track_info['device_name']}"
            ),
            "track_info": track_info
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

def spotify_play(client_id: str, client_secret: str, redirect_uri: str) -> Dict[str, Any]:
    """Resume playback"""
    try:
        client = create_spotify_auth(client_id, client_secret, redirect_uri)
        current = client.current_playback()
        if current and current.get('is_playing'):
            return {"status": "error", "message": "Spotify is already playing"}
        client.start_playback()
        return {"status": "success", "message": "Playback resumed"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def spotify_pause(client_id: str, client_secret: str, redirect_uri: str) -> Dict[str, Any]:
    """Pause playback"""
    try:
        client = create_spotify_auth(client_id, client_secret, redirect_uri)
        current = client.current_playback()
        if current and not current.get('is_playing'):
            return {"status": "error", "message": "Spotify is already paused"}
        client.pause_playback()
        return {"status": "success", "message": "Playback paused"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def spotify_next_track(client_id: str, client_secret: str, redirect_uri: str) -> Dict[str, Any]:
    """Skip to next track"""
    try:
        client = create_spotify_auth(client_id, client_secret, redirect_uri)
        client.next_track()
        return {"status": "success", "message": "Skipped to next track"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def spotify_previous_track(client_id: str, client_secret: str, redirect_uri: str) -> Dict[str, Any]:
    """Go back to previous track"""
    try:
        client = create_spotify_auth(client_id, client_secret, redirect_uri)
        client.previous_track()
        return {"status": "success", "message": "Went back to previous track"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def spotify_set_volume(client_id: str, client_secret: str, redirect_uri: str, volume: int) -> Dict[str, Any]:
    """Set playback volume"""
    try:
        if not 0 <= volume <= 100:
            return {"status": "error", "message": "Volume must be between 0 and 100"}
        
        client = create_spotify_auth(client_id, client_secret, redirect_uri)
        client.volume(volume)
        return {"status": "success", "message": f"Volume set to {volume}%"}
    except Exception as e:
        return {"status": "error", "message": str(e)} 
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from backend.config import settings
import os

class SpotifyAuthManager:
    """Handles Spotify authentication for Smood"""
    
    # Scopes needed for Smood functionality
    SMOOD_SCOPES = [
        # Reading data
        "user-read-private",
        "user-read-email",
        "user-top-read",
        "user-read-recently-played",
        "user-library-read",
        
        # Playlist management
        "playlist-read-private",
        "playlist-read-collaborative",
        "playlist-modify-public",
        "playlist-modify-private",
        
        # Playback (optional)
        "user-read-playback-state",
        "user-read-currently-playing"
    ]
    
    def __init__(self):
        self.cache_path = ".spotify_cache"
        
    def get_auth_manager(self, cache_path=None):
        """Get Spotify OAuth manager"""
        return SpotifyOAuth(
            client_id=settings.spotify_client_id,
            client_secret=settings.spotify_client_secret,
            redirect_uri=settings.spotify_redirect_uri,
            scope=" ".join(self.SMOOD_SCOPES),
            cache_path=cache_path or self.cache_path,
            open_browser=False  # We'll handle this manually
        )
    
    def get_client_for_user(self, auth_manager):
        """Get authenticated Spotify client for a user"""
        return spotipy.Spotify(auth_manager=auth_manager)
    
    def get_app_client(self):
        """Get client credentials (app-only) client"""
        client_credentials = SpotifyClientCredentials(
            client_id=settings.spotify_client_id,
            client_secret=settings.spotify_client_secret
        )
        return spotipy.Spotify(client_credentials_manager=client_credentials)
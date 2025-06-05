import sys
sys.path.append('..')

from backend.config import settings
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def test_spotify_connection():
    """Test if Spotify credentials are working"""
    try:
        client_credentials_manager = SpotifyClientCredentials(
            client_id=settings.spotify_client_id,
            client_secret=settings.spotify_client_secret
        )
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        
        # Try to get a track
        track = sp.track('3n3Ppam7vgaVa1iaRUc9Lp')
        print(f"Spotify connection successful!")
        print(f"Test track: {track['name']} by {track['artists'][0]['name']}")
        
        # Get audio features
        features = sp.audio_features(track['id'])[0]
        print(f"\nAudio features:")
        print(f"  Energy: {features['energy']}")
        print(f"  Valence: {features['valence']}")
        print(f"  Danceability: {features['danceability']}")
        
        return True
        
    except Exception as e:
        print(f"Spotify connection failed wah-wah: {str(e)}")
        print("\nMake sure you have:")
        print("1. Created a Spotify app at https://developer.spotify.com/dashboard")
        print("2. Added your Client ID and Secret to the .env file")
        return False

if __name__ == "__main__":
    test_spotify_connection()
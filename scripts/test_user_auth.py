import sys
sys.path.append('..')

from backend.services.spotify.auth import SpotifyAuthManager
import webbrowser

def test_user_authentication():
    """Test Spotify user authentication flow"""
    print("Testing Smood User Authentication...")
    
    auth_manager_service = SpotifyAuthManager()
    auth_manager = auth_manager_service.get_auth_manager()
    
    # Get authorization URL
    auth_url = auth_manager.get_authorize_url()
    print(f"\n📱 Please visit this URL to authorize Smood:")
    print(auth_url)
    
    # Try to open in browser
    try:
        webbrowser.open(auth_url)
        print("\nOpened browser. Please authorize Smood.")
    except:
        print("\nCouldn't open browser automatically.")
    
    # Get the response URL
    print("\nAfter authorizing, you'll be redirected to a URL starting with:")
    print(f"   {auth_manager.redirect_uri}?code=...")
    response_url = input("\nPaste the complete URL here: ").strip()
    
    try:
        # Parse the response
        code = auth_manager.parse_response_code(response_url)
        
        # Get access token
        token_info = auth_manager.get_access_token(code)
        
        # Create client with user auth
        sp = auth_manager_service.get_client_for_user(auth_manager)
        
        # Test various endpoints
        print("\nAuthentication successful! Testing access...")
        
        # Get user info
        user = sp.current_user()
        print(f"\nLogged in as: {user['display_name']} ({user['email']})")
        
        # Get top tracks
        top_tracks = sp.current_user_top_tracks(limit=5, time_range='short_term')
        print("\nYour top tracks:")
        for i, track in enumerate(top_tracks['items'], 1):
            print(f"   {i}. {track['name']} - {track['artists'][0]['name']}")
        
        # Audio features are deprecated
        if top_tracks['items']:
            track_id = top_tracks['items'][0]['id']
            features = sp.audio_features([track_id])[0]
            print(f"\nAudio features for '{top_tracks['items'][0]['name']}':")
            print(f"   Energy: {features['energy']:.2f}")
            print(f"   Valence: {features['valence']:.2f}")
            print(f"   Danceability: {features['danceability']:.2f}")
            print(f"   Tempo: {features['tempo']:.0f} BPM")
        
        print("\nAll Smood features are accessible!")
        
    except Exception as e:
        print(f"\nAuthentication failed wah-wah: {e}")
        print("\nMake sure:")
        print("1. You authorized the app")
        print("2. You copied the complete redirect URL")
        print("3. Your redirect URI in Spotify app settings matches the .env file")

if __name__ == "__main__":
    test_user_authentication()
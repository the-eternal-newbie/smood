import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

class Settings(BaseSettings):
    # Spotify
    spotify_client_id: str = os.getenv("SPOTIFY_CLIENT_ID", "")
    spotify_client_secret: str = os.getenv("SPOTIFY_CLIENT_SECRET", "")
    spotify_redirect_uri: str = os.getenv("SPOTIFY_REDIRECT_URI", "http://127.0.0.1:8000/callback")
    
    # Google Cloud
    google_cloud_project: str = os.getenv("GOOGLE_CLOUD_PROJECT", "")
    google_application_credentials: str = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "")
    
    # API
    api_port: int = int(os.getenv("API_PORT", "8000"))
    api_host: str = os.getenv("API_HOST", "0.0.0.0")
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "")
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "43200"))
    
    # Database
    firestore_database: str = os.getenv("FIRESTORE_DATABASE", "(default)")
    bigquery_dataset: str = os.getenv("BIGQUERY_DATASET", "mood_music_data")
    
    # Development
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
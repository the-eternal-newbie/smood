# Smood - Spotify Mood Discovery Engine

A machine learning-powered music discovery platform that analyzes listening patterns, genres, and external metadata to provide mood-based recommendations and personalized playlists.

## Table of Contents

> TBD

## Overview

Smood combines Spotify's music catalog with advanced pattern recognition and mood analysis to create personalized music experiences. Unlike traditional recommendation systems that rely solely on audio features, Smood employs a hybrid approach combining:

- Genre-based mood mapping
- External metadata enrichment
- User behavior pattern analysis
- Time-contextual recommendations
- Collaborative filtering techniques

## Features

### Core Functionality

- **Mood-Based Discovery**: Automatically classifies tracks into mood categories (energetic, calm, happy, melancholic, focused, party)
- **Smart Clustering**: Groups similar tracks using genre patterns and user behavior
- **Contextual Recommendations**: Adapts suggestions based on time of day, listening history, and user state
- **Playlist Generation**: Creates mood-specific playlists with optimized track ordering
- **Mashup Previews**: Generates audio previews that blend multiple tracks for quick mood sampling

### Technical Features

- RESTful API built with FastAPI
- Real-time data processing with Google Cloud Firestore
- Analytics pipeline using BigQuery
- Scalable microservices architecture
- JWT-based authentication
- Comprehensive logging and monitoring

## Technical Architecture

### System Components

> TBD

### Data Flow

1. User authentication via Spotify OAuth 2.0
2. Fetch user's listening history and saved tracks
3. Analyze genres and enrich with external metadata
4. Apply mood classification algorithms
5. Generate personalized recommendations
6. Track user interactions for continuous improvement

## Data Analysis Methodology

### Genre-Based Mood Mapping

Smood uses a comprehensive genre-to-mood mapping system based on music psychology research. Each genre is assigned scores across multiple dimensions:

- **Energy**: Perceived intensity and activity level (0.0 - 1.0)
- **Valence**: Emotional positivity/negativity (0.0 - 1.0)
- **Danceability**: Rhythmic movement inducement (0.0 - 1.0)


### Mood Classification Algorithm

```python
# Simplified mood inference logic
if energy > 0.7 and valence > 0.7:
    mood = 'euphoric'
elif energy > 0.7 and valence < 0.4:
    mood = 'aggressive'
elif energy < 0.4 and valence > 0.6:
    mood = 'peaceful'
elif energy < 0.4 and valence < 0.4:
    mood = 'melancholic'
```



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Spotify Web API for music data access
- Last.fm for metadata enrichment
- Google Cloud Platform for infrastructure
- Music Information Retrieval community for research foundations

import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Constants
NUM_USERS = 80
NUM_ARTISTS = 30
NUM_ALBUMS = 35
NUM_SONGS = 500
NUM_INTERACTIONS = 300
NUM_PLAYLISTS = 50
NUM_PLAYLIST_SONGS = 200

# 1. Users Table
users = []
for user_id in range(1, NUM_USERS + 1):
    users.append({
        'user_id': user_id,
        'username': fake.user_name(),
        'email': fake.unique.email(),
        'subscription_type': random.choice(['Free', 'Premium']),
        'registration_date': fake.date_between(start_date='-3y', end_date='today')
    })

# 2. Artists Table
artists = []
genres = ['Pop', 'Hip-Hop', 'Afrobeats', 'RnB', 'Rock', 'Jazz', 'Classical']
for artist_id in range(1, NUM_ARTISTS + 1):
    artists.append({
        'artist_id': artist_id,
        'name': fake.name(),
        'genre': random.choice(genres),
        'debut_year': random.randint(2000, 2022)
    })

# 3. Albums Table
albums = []
for album_id in range(1, NUM_ALBUMS + 1):
    artist = random.choice(artists)
    albums.append({
        'album_id': album_id,
        'title': fake.sentence(nb_words=2).replace('.', ''),
        'artist_id': artist['artist_id'],
        'release_year': random.randint(2010, 2023),
        'genre': artist['genre']
    })

# 4. Songs Table
songs = []
for song_id in range(1, NUM_SONGS + 1):
    artist = random.choice(artists)
    album = random.choice(albums)
    duration = timedelta(minutes=random.randint(2, 5), seconds=random.randint(0, 59))
    songs.append({
        'song_id': song_id,
        'title': fake.sentence(nb_words=3).replace('.', ''),
        'artist_id': artist['artist_id'],
        'album_id': album['album_id'],
        'release_year': album['release_year'],
        'duration': (datetime.min + duration).time()
    })

# 5. User Interaction Table
interactions = []
for interaction_id in range(1, NUM_INTERACTIONS + 1):
    interactions.append({
        'interaction_id': interaction_id,
        'user_id': random.randint(1, NUM_USERS),
        'song_id': random.randint(1, NUM_SONGS),
        'listen_time': fake.time_object(),
        'rating': random.randint(1, 5)
    })

# 6. Playlists Table
playlists = []
for playlist_id in range(1, NUM_PLAYLISTS + 1):
    playlists.append({
        'playlist_id': playlist_id,
        'user_id': random.randint(1, NUM_USERS),
        'name': fake.word().capitalize() + " Playlist",
        'creation_date': fake.date_between(start_date='-2y', end_date='today')
    })

# 7. Playlist Songs Table
playlist_songs = []
for _ in range(NUM_PLAYLIST_SONGS):
    playlist_songs.append({
        'playlist_id': random.randint(1, NUM_PLAYLISTS),
        'song_id': random.randint(1, NUM_SONGS),
    })

# Convert to DataFrames
df_users = pd.DataFrame(users)
df_artists = pd.DataFrame(artists)
df_albums = pd.DataFrame(albums)
df_songs = pd.DataFrame(songs)
df_interactions = pd.DataFrame(interactions)
df_playlists = pd.DataFrame(playlists)
df_playlist_songs = pd.DataFrame(playlist_songs)

# Export to Excel
"""
with pd.ExcelWriter('music_data.xlsx') as writer:
    df_users.to_excel(writer, sheet_name='Users', index=False)
    df_artists.to_excel(writer, sheet_name='Artists', index=False)
    df_albums.to_excel(writer, sheet_name='Albums', index=False)
    df_songs.to_excel(writer, sheet_name='Songs', index=False)
    df_interactions.to_excel(writer, sheet_name='UserInteraction', index=False)
    df_playlists.to_excel(writer, sheet_name='Playlists', index=False)
    df_playlist_songs.to_excel(writer, sheet_name='PlaylistSongs', index=False)
"""

# Export to individual CSV files (for PostgreSQL import)
df_users.to_csv("users.csv", index=False)
df_artists.to_csv("artists.csv", index=False)
df_albums.to_csv("albums.csv", index=False)
df_songs.to_csv("songs.csv", index=False)
df_interactions.to_csv("user_interaction.csv", index=False)
df_playlists.to_csv("playlists.csv", index=False)
df_playlist_songs.to_csv("playlist_songs.csv", index=False)

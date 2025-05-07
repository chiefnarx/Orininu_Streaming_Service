-- Users Table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    subscription_type VARCHAR(20) CHECK (subscription_type IN ('Free', 'Premium')),
    registration_date DATE NOT NULL
);

-- Artists Table
CREATE TABLE artists (
    artist_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    genre VARCHAR(50),
    debut_year INT
);

-- Albums Table
CREATE TABLE albums (
    album_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    artist_id INT REFERENCES artists(artist_id) ON DELETE CASCADE,
    release_year INT NOT NULL,
    genre VARCHAR(50)
);

-- Songs Table
CREATE TABLE songs (
    song_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    artist_id INT REFERENCES artists(artist_id) ON DELETE CASCADE,
    album_id INT REFERENCES albums(album_id) ON DELETE CASCADE,
    release_year INT NOT NULL,
    duration TIME NOT NULL
);

-- User Interaction Table
CREATE TABLE user_interaction (
    interaction_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    song_id INT REFERENCES songs(song_id) ON DELETE CASCADE,
    listen_time TIME NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5)
);

-- Playlists Table
CREATE TABLE playlists (
    playlist_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    creation_date DATE NOT NULL
);

-- Playlist Songs Table (Associative Table)
CREATE TABLE playlist_songs (
    playlist_id INT REFERENCES playlists(playlist_id) ON DELETE CASCADE,
    song_id INT REFERENCES songs(song_id) ON DELETE CASCADE,
    PRIMARY KEY (playlist_id, song_id)
);

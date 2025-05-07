-- Pgadmin isn't assigning unique keys to new informations, so I have to implment something like an "enforcer."
-- Ensuring Pgadmin picks a new and unique id for each new artist, album, and song I add.
SELECT setval('artists_artist_id_seq', (SELECT MAX(artist_id) FROM artists) + 1);
SELECT setval('albums_album_id_seq', (SELECT MAX(album_id) FROM albums) + 1);
SELECT setval('songs_song_id_seq', (SELECT MAX(song_id) FROM songs) + 1);


-- Adding a new artist
INSERT INTO artists (name, genre, debut_year)
VALUES ('Chief Narx', 'Mixed', 2025)

-- Adding an album for Chief Narx
INSERT INTO albums (title, artist_id, release_year, genre) 
VALUES ('Homecoming', 
		(SELECT artist_id FROM artists WHERE name = 'Chief Narx'), 
		2030, 'Mixed');

-- Adding a song for Chief Narx and his Homecoming album
INSERT INTO songs (title, artist_id, album_id, release_year, duration) 
VALUES ('', 
        (SELECT artist_id FROM artists WHERE name = 'Chief Narx'),
        (SELECT album_id FROM albums WHERE title = 'Homecoming'),
        2030, '03:45');

-- Forgot to add the title of the song I inserted above, so I have to run an update here
UPDATE songs 
SET title = 'Homecoming'
WHERE artist_id = (SELECT artist_id FROM artists WHERE name = 'Chief Narx')
AND album_id = (SELECT album_id FROM albums WHERE title = 'Homecoming')
AND release_year = 2030
AND duration = '03:45';






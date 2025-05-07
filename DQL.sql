-- Finding the new artist added
SELECT * 
FROM artists 
WHERE name = 'Chief Narx';

-- Finding another artist
SELECT * 
FROM artists 
WHERE artist_id = '28';

-- Finding the 5 Most Played Artists by calculating the total play count
SELECT ar.name AS artist -- Assigning aliases
COUNT(i.song_id) AS total_plays
FROM user_interaction i
JOIN songs s ON i.song_id = s.song_id -- Shared column (song_id) between user-interctions table and songs table
JOIN artists ar ON s.artist_id = ar.artist_id -- Shared column (artist_id) between songs table and artists table
GROUP BY ar.name
ORDER BY total_plays DESC
LIMIT 5;

-- Finding artists and their albums and songs
SELECT a.title AS album, s.title AS song, ar.name AS artist, a.release_year
FROM songs s
JOIN albums a ON s.album_id = a.album_id
JOIN artists ar ON a.artist_id = ar.artist_id
ORDER BY a.release_year ASC;

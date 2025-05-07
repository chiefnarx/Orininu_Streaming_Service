-- Create sync tracking table
CREATE TABLE sync_queue (
    id SERIAL PRIMARY KEY,
    table_name TEXT,
    record_id TEXT,
    operation TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Function to detect and log changes
CREATE OR REPLACE FUNCTION log_changes() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO sync_queue (table_name, record_id, operation)
    VALUES (TG_TABLE_NAME, NEW.song_id, TG_OP);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers to monitor all tables
CREATE TRIGGER sync_users AFTER INSERT OR UPDATE OR DELETE ON users
FOR EACH ROW EXECUTE FUNCTION log_changes();

CREATE TRIGGER sync_artists AFTER INSERT OR UPDATE OR DELETE ON artists
FOR EACH ROW EXECUTE FUNCTION log_changes();

CREATE TRIGGER sync_albums AFTER INSERT OR UPDATE OR DELETE ON albums
FOR EACH ROW EXECUTE FUNCTION log_changes();

CREATE TRIGGER sync_songs AFTER INSERT OR UPDATE OR DELETE ON songs
FOR EACH ROW EXECUTE FUNCTION log_changes();

CREATE TRIGGER sync_user_interaction AFTER INSERT OR UPDATE OR DELETE ON user_interaction
FOR EACH ROW EXECUTE FUNCTION log_changes();

CREATE TRIGGER sync_playlists AFTER INSERT OR UPDATE OR DELETE ON playlists
FOR EACH ROW EXECUTE FUNCTION log_changes();

CREATE TRIGGER sync_playlist_songs AFTER INSERT OR UPDATE OR DELETE ON playlist_songs
FOR EACH ROW EXECUTE FUNCTION log_changes();

-- Check current database
SELECT current_database();

-- Insert test song into `songs` table
INSERT INTO songs (title, artist_id, album_id, release_year, duration) 
VALUES ('Test Track', 1, 1, 2010, '00:03:30');

-- Verify changes in sync table
SELECT * FROM sync_queue ORDER BY timestamp ASC;

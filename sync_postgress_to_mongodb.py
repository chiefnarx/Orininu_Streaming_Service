import psycopg2
import pymongo

# Connect to PostgreSQL
pg_conn = psycopg2.connect(
    dbname='Orininu Streaming Service',
    user="postgres",
    password="MongoDB4luv",
    host="localhost",
    port="5432"
)
pg_cursor = pg_conn.cursor()

# Connect to MongoDB Atlas
mongo_client = pymongo.MongoClient("mongodb+srv://ameereking:bJx3Tov81KBpaeJ2@cluster0.jeaqbgq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
mongo_db = mongo_client["OrininuStreamingDB"]

# Check for new changes in PostgreSQL sync table
pg_cursor.execute("SELECT * FROM sync_queue ORDER BY timestamp ASC")
changes = pg_cursor.fetchall()
print("🔍 Changes to Process for MongoDB:", changes)  # Debugging output

# Correct primary keys for different tables
primary_keys = {
    "songs": "song_id",
    "artists": "artist_id",
    "albums": "album_id",
    "users": "user_id",
    "playlists": "playlist_id",
    "playlist_songs": "playlist_song_id"
}

for change in changes:
    table, record_id, operation, timestamp = change[1], change[2], change[3], change[4]
    mongo_collection = mongo_db[table]
    primary_key = primary_keys.get(table, "id")  # Default to "id" if undefined

    if operation in ["INSERT", "UPDATE"]:
        pg_cursor.execute(f"SELECT * FROM {table} WHERE {primary_key} = %s", (record_id,))
        record = pg_cursor.fetchone()
        
        if record:
            column_names = [desc[0] for desc in pg_cursor.description]
            record_dict = dict(zip(column_names, record))

            # Convert `duration` field to string if present
            if "duration" in record_dict:
                record_dict["duration"] = str(record_dict["duration"])  # Convert time to string

            if operation == "INSERT":
                mongo_collection.insert_one(record_dict)
            elif operation == "UPDATE":
                mongo_collection.update_one({primary_key: record_id}, {"$set": record_dict})

    elif operation == "DELETE":
        mongo_collection.delete_one({primary_key: record_id})

# Clear sync queue after processing
pg_cursor.execute("DELETE FROM sync_queue")
pg_conn.commit()

print("🔥 PostgreSQL → MongoDB Sync Complete!")

pg_cursor.close()
pg_conn.close()

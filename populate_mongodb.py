from pymongo import MongoClient

# Connect to MongoDB Atlas
mongo_client = MongoClient("mongodb+srv://ameereking:bJx3Tov81KBpaeJ2@cluster0.jeaqbgq.mongodb.net/OrininuStreamingDB?retryWrites=true&w=majority&appName=Cluster0")
mongo_db = mongo_client["OrininuStreamingDB"]

# Sample data for MongoDB collections
data = {
    "artists": [
        {"name": "DJ Khaled", "genre": "Hip-Hop", "debut_year": 2010}
    ],

    "albums": [
        {"title": "We The Best", "artist": "DJ Khaled", "year": 2010}
    ],
    
    "users": [
        {"username": "ameer123", "email": "ameer@gmail.com"},
        {"username": "guest_user", "email": "guest@example.com"}
    ]
}

# Inserting new data into MongoDB
for collection, records in data.items():
    mongo_collection = mongo_db[collection]
    mongo_collection.insert_many(records)
    print(f"Inserted {len(records)} records into {collection}!")

print("🔥 Fresh MongoDB setup complete! No Firebase involved!")

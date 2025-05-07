from pymongo import MongoClient

# Connect to MongoDB Atlas
mongo_client = MongoClient("mongodb+srv://ameereking:bJx3Tov81KBpaeJ2@cluster0.jeaqbgq.mongodb.net/OrininuStreamingDB?retryWrites=true&w=majority&appName=Cluster0")
mongo_db = mongo_client["OrininuStreamingDB"]

# Define collections to retrieve data from
collections = ["artists", "albums", "users"]

# Retrieve and display data from each collection
for collection_name in collections:
    mongo_collection = mongo_db[collection_name]
    documents = mongo_collection.find()

    print(f"\nData from '{collection_name}':")
    for doc in documents:
        print(doc)

print("\n🔥 Data retrieval from MongoDB complete!")

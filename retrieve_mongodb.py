from pymongo import MongoClient

# Connecting to MongoDB Atlas
mongo_client = MongoClient("mongodb+srv://ameereking:bJx3Tov81KBpaeJ2@cluster0.jeaqbgq.mongodb.net/OrininuStreamingDB?retryWrites=true&w=majority&appName=Cluster0")
mongo_db = mongo_client["OrininuStreamingDB"]

collections = ["artists", "albums", "users"]

for collection_name in collections:
    mongo_collection = mongo_db[collection_name]
    documents = mongo_collection.find()

    print(f"\nData from '{collection_name}':")
    for doc in documents:
        print(doc)


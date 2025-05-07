from pymongo import MongoClient

client = MongoClient("mongodb+srv://ameereking:bJx3Tov81KBpaeJ2@cluster0.jeaqbgq.mongodb.net/OrininuStreamingDB?retryWrites=true&w=majority&appName=Cluster0")

db = client["OrininuStreamingDB"]

# Testing connection by listing collections
collections = db.list_collection_names()

# It worked.

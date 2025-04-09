from pymongo import MongoClient
import os

MONGO_HOST = os.getenv("MONGO_HOST", "mongo")  # Le nom du service Mongo dans docker-compose
client = MongoClient(f"mongodb://{MONGO_HOST}:27017/")
db = client["lycees_db"]
collection = db["lycees"]

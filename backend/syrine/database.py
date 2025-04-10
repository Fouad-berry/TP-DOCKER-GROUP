# database.py

from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017/")
db = client["ma_base"]
collection = db["ma_collection"]

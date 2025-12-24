
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://ishita:test12345@cluster0.a1n7gna.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client["blog_db"]
blogs_collection = db["blogs"]

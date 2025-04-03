import pymongo
from config import Config

client = pymongo.MongoClient(Config.MONGO_URI)
db = client["MoxiBot"]
filters_collection = db["filters"]

def add_filter(keyword, reply_text):
    filters_collection.update_one({"keyword": keyword}, {"$set": {"reply": reply_text}}, upsert=True)

def get_filter(keyword):
    result = filters_collection.find_one({"keyword": keyword})
    return result["reply"] if result else None

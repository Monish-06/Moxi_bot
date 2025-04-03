import pymongo
from config import Config

client = pymongo.MongoClient(Config.MONGO_URI)
db = client["MoxiBot"]
filestore_collection = db["filestore"]

def save_file(file_id, message):
    file_data = {
        "file_id": file_id,
        "file_name": message.document.file_name if message.document else None,
        "size": message.document.file_size if message.document else None,
    }
    filestore_collection.insert_one(file_data)

def get_file(file_id):
    return filestore_collection.find_one({"file_id": file_id})

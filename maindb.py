from pymongo import MongoClient
from bson import ObjectId
import os




uri=os.getenv("MONGO_URI")
client = MongoClient(uri)
db = client["Haris__"]



def re_mogo(tname):
    global db
    return db[tname]


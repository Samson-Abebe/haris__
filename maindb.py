from pymongo import MongoClient
from bson import ObjectId
import os
#https://gist.github.com/ScriptBytes/2c0b8658fe6e16467f697f76be06f7bd

uri =os.getenv("MONGO_URI"),


client = MongoClient(uri)
db = client["Haris__"]
db_=client["Haris"]
transactions = db["transactions"]

def re_mogo(tname):
    global db
    return db[tname]
def re_mogo_(tname):
    global db_
    return db_[tname]

# from pymongo import MongoClient
# from bson import ObjectId

# uri = "mongodb+srv://samsonabebe:YOUR_PASSWORD@cluster0022.zcfqojs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0022"

# client = MongoClient(uri)

# db = client["Haris__"]
# db_ = client["Haris"]

# transactions = db["transactions"]

# def re_mogo(tname):
#     return db[tname]

# def re_mogo_(tname):
#     return db_[tname]


# #xlzNQkseRg8M5Yy3


# from pymongo import MongoClient
# from pymongo.server_api import ServerApi

# uri = "mongodb+srv://samsonabebe:xlzNQkseRg8M5Yy3@cluster0022.zcfqojs.mongodb.net/?appName=Cluster0022"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
# from pymongo import MongoClient

# # Local MongoDB
# local_client = MongoClient(
#     "mongodb://mongoadmin:LikeAndSubscribe@localhost:27017/"
# )

# # Atlas MongoDB
# atlas_client = MongoClient(uri)

# # Source and destination databases
# local_db = local_client["Haris__"]
# atlas_db = atlas_client["Haris__"]

# # Copy all collections
# for collection_name in local_db.list_collection_names():
#     print(f"Copying {collection_name}...")

#     source_collection = local_db[collection_name]
#     dest_collection = atlas_db[collection_name]

#     documents = list(source_collection.find({}))

#     if documents:
#         # Optional: clear destination collection first
#         dest_collection.delete_many({})

#         dest_collection.insert_many(documents)
#         print(f"  Copied {len(documents)} documents")
#     else:
#         print("  Collection is empty")

# print("Migration completed.")
import pymongo
import os
import datetime
from info.info import environ_set

environ_set()
# Create a connection to the local database:
connection = pymongo.MongoClient(os.getenv("MONGO_LOCAL"))

# Create a connection to the atlas database:
print(os.environ)
print(os.getenv("MONGO_ATLAS"))
connection_url = os.environ.get("MONGO_ATLAS")
connection_url = connection_url.replace("<password>", os.getenv("MONGO_PASS"))
connection_url = connection_url.replace("<dbname>", os.getenv("MONGO_DATABASE"))
print(connection_url)
connection_atlas = pymongo.MongoClient(connection_url)

# Choose the connection to manipulate:
db = connection_atlas["python-database"]

# Choose the collection to manipulate:
collection = db['python-collection']

# Create the document:
python_document1 = {"Property1": "A String",
                    "Property2": 123,
                    "Property3": ["An", "Array"],
                    "Property4": datetime.datetime.now()}

# Insert a document:
db.collection.insert_one(python_document1)
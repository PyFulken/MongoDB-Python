from mongo_connector import connection_set

# Use the connection function made in the file mongo_connector.py too create the db instance.
db = connection_set(False, "python-database")

db.createCollection("python_collection_validated", {
    "validator": {"$jsonSchema": {"bsonType": "object", "required": ["random_number", "Date"], "properties": {
        "random_number": {"bsonType": "int", "description": "Must be int and it's required."},
        "Date": {"bsonType": "Date", "description": "Must be a Date object and it's required."}}}}})



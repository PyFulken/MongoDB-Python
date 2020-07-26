from create_data import create_documents
from mongo_connector import connection_set

# Use the connection function made in the file mongo_connector.py too create the db instance.
db = connection_set(False, "python-database")

# Create x amount of documents to insert using code done in create_data.py
# python_document = create_documents(10)

# Insert documents:
# --------WARNING--------
# The name between db. and .insert is the collection name to insert into.
# If it doesn't exist, it will be created, misplacing the documents.
# db.python_collection_2.insert_many(python_document)

# Search queries:
# --------WARNING--------
# To receive and handle collections they must be firstly instanced with:
# correct_collection_name = db["desired_collection_name"]
python_collection = db["python_collection"]
# For deeper and finer searches a query must be passed as the first argument in find(). Queries are dictionaries.
query = {"_id": {"$lte": 10}}
received_document = python_collection.find(query)
for i in received_document:
    print(i)

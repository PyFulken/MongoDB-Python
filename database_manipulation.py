from create_data import create_documents
from mongo_connector import connection_set

# Use the connection function made in the file mongo_connector.py too create the db instance.
db = connection_set(False, "python-database")

# Create x amount of documents to insert using code done in create_data.py
python_document = create_documents(10)

# Insert documents:
# --------WARNING--------
# The name between db. and .insert is the collection name to insert into.
# If it doesn't exist, it will be created, misplacing the documents.
#db.python_collection_2.insert_many(python_document)

# Search queries:

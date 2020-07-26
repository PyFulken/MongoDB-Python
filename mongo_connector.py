import pymongo
import os
from info.info import environ_set


def connection_set(local, database):
    """
    Sets a connection to a Mongo database.
    Requires the following environmental variables to be set:
    MONGO_LOCAL: URL to local Mongo instance.
    MONGO_ATLAS: URL to Atlas hosted Mongo instance.
    MONGO_PASS: Password to the Atlas user.
    MONGO_DATABASE: Database to connect to.
    Parameters:
     local (boolean): True to connect to local Mongo instance.
     database (string): The database to connect to.
    Returns:
         database: A fully connected database connection instance.
    """
    # Set Environmental Variables
    environ_set()
    if local:
        # Create a connection to the local database:
        connection = pymongo.MongoClient(os.getenv("MONGO_LOCAL"))
    else:
        # Create a connection to the atlas database:
        connection_url = os.environ.get("MONGO_ATLAS")
        connection_url = connection_url.replace("<password>", os.getenv("MONGO_PASS"))
        connection_url = connection_url.replace("<dbname>", os.getenv("MONGO_DATABASE"))
        connection = pymongo.MongoClient(connection_url)
    db = connection[database]
    return db

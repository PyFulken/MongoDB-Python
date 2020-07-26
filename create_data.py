import datetime
from random import randint


def create_documents(amount):
    """
    Create a list with a variable amount of documents with random information.

    Parameters:
     amount (int): The amount of documents to be generated.

    Returns:
         list: An array of documents.
    """
    # Create the document:
    python_document = []
    for i in range(amount):
        random_date = datetime.datetime(randint(1990, 2020), randint(1, 12), randint(1, 28), randint(0, 23),
                                        randint(0, 59), randint(0, 59))
        python_document.append({"_id": i,
                                "random_number": randint(0, 500),
                                "Date": random_date.strftime("%Y/%m/%d %H:%M:%S")}
                               )
    return python_document

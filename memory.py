import os
from google.cloud import firestore

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'extended-signal-464909-k2-19723a7eff2c.json'
db = firestore.Client()

def get_user_memory(user_id: int) -> dict:
    """Retrieves a user's memory from Firestore
    Fetches the document corresponding to the given user ID

    Args:
        user_id (int): Unique Telegram chat id 

    Returns:
        dict: A dictionary containing the user's memory data if it exists,
            else an empty dictionary
    """
    doc_ref = db.collection('users').document(str(user_id))
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return {}

def update_user_memory(user_id: int, key: str, value: any) -> None:
    """Updates a user's memory in Firestore
    Adds or updates a key-value pair within the specified user's document.
    If the document does not exist, it is created

    Args:
        user_id (int): Unique Telegram chat id
        key (str): Name of the field to update or add in the user's memory
        value (any): Value for specified field
    """
    user_ref = db.collection('users').document(str(user_id))
    user_ref.set({key: value}, merge=True)
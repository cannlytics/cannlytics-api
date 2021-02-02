"""
Firebase | Cannlytics Website
Created: 2/1/2021
"""
from django.utils.crypto import get_random_string
from firebase_admin import auth, firestore, initialize_app, storage
from google.cloud.firestore import ArrayUnion, ArrayRemove
from uuid import uuid4


initialize_app()


#------------------------------------------------------------#
# Firestore helpers
#------------------------------------------------------------#


def create_reference(database, reference):
    """Create a database reference for a given path."""
    ref = database
    parts = reference.split('/')
    for i in range(len(parts)):
        part = parts[i]
        if i % 2:
            ref = ref.document(part)
        else:
            ref = ref.collection(part)
    return ref


def get_keywords(string):
    """Get keywords for a given string."""
    keywords = string.lower().split(' ')
    keywords = list(filter("", keywords))
    return keywords


def add_to_array(ref, field, value):
    """Add an element to a given field for a given reference."""
    database = firestore.client()
    doc = create_reference(database, ref)
    doc.update({field: ArrayUnion([value])})


def remove_from_array(ref, field, value):
    """Remove an element from a given field for a given reference."""
    database = firestore.client()
    doc = create_reference(database, ref)
    doc.update({field: ArrayRemove([value])})


def update_document(ref, values):
    """Update a given document."""
    database = firestore.client()
    doc = create_reference(database, ref)
    doc.set(values, merge=True)


def get_document(ref):
    """Get a given document."""
    database = firestore.client()
    doc = create_reference(database, ref)
    data = doc.get()
    if data is None:
        return {}
    else:
        return data.to_dict()


def get_collection(ref, limit=None, order_by=None, desc=False, filters=[]):
    """Get documents from a collection."""
    docs = []
    database = firestore.client()
    collection = create_reference(database, ref)
    if filters:
        for filter in filters:
            collection = collection.where(filter["key"], filter["operation"], filter["value"])
    if order_by and desc:
        collection = collection.order_by(order_by, direction='DESCENDING')
    elif order_by:
        collection = collection.order_by(order_by)
    if limit:
        collection = collection.limit(limit)
    query = collection.stream() # Only handles streams less than 2 mins.
    for doc in query:
        data = doc.to_dict()
        docs.append(data)
    return docs


#------------------------------------------------------------#
# Authentication helpers
#------------------------------------------------------------#


def create_account(name, email, notification=True):
    """
    Given user name and email, create an account if the email isn't being used
    by an existing account.
    """
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$-_'
    password = get_random_string(42, chars)
    # Optional: Try to get photo_url from gravatar.
    try:
        user = auth.create_user(
            uid=str(uuid4()),
            email=email,
            email_verified=False,
            password=password,
            display_name=name,
            photo_url=None,
            disabled=False
        )
        return user, password
    except:
        return None, None


#------------------------------------------------------------#
# Storage helpers
#------------------------------------------------------------#


def download_file(source_blob_name, destination_file_name):
    """Downloads a file from Firebase Storage."""
    bucket = storage.bucket(name="cannlytics.appspot.com") # TODO: Get from .env
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(
        "Blob {} downloaded to {}.".format(
            source_blob_name, destination_file_name
        )
    )


def upload_file(destination_blob_name, source_file_name):
    """Upload file to Firebase Storage."""
    bucket = storage.bucket(name="cannlytics.appspot.com") # TODO: Get from .env
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )


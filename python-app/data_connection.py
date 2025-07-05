from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pathlib import Path
import datetime

class BlobStorage:

    def __init__(self):

        '''
        Initalize
        '''

        # container name
        self.CONTAINER_NAME = "video"

        
        # sas token
        load_dotenv("passwords.env")
        self.sas_token = os.getenv("SAS_TOKEN")

    def data_push(self, path, name):

        '''
        Push data to blob
        '''

        # Create a BlobServiceClient
        blob_service_client = BlobServiceClient(account_url="https://w3bapp.blob.core.windows.net", credential=self.sas_token)

        # Get a ContainerClient
        container_client = blob_service_client.get_container_client(self.CONTAINER_NAME)

        # Create a BlobClient
        blob_client = container_client.get_blob_client(name)

        # Open the local video file and upload it
        with open(path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        
        # If it works
        print(f"✅ Uploaded '{path}' to container '{self.CONTAINER_NAME}' as blob '{name}'.")


class MongoConnection:
    def __init__(self):
        pass

    def connect_to_database(self):

        # mongo uri
        load_dotenv("passwords.env")
        uri = os.getenv("mongo_uri")

        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))

        # Ping to confirm a successful connection
        
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
            
        return client.prod

    def video_meta_data(self,id):

        # Connect to database
        db = self.connect_to_database()

        try:

            # post this information
            post = {
                    "author": "Ethan",
                    "id":id,
                    "text": "Test post",
                    "tags": ["test", "video"],
                    "date": datetime.datetime.now(tz=datetime.timezone.utc),
                }
            
            video_meta = db.video_meta
            out = video_meta.insert_one(post).inserted_id
                    
            print(out)
            
            return f"Post was successful: {out}"
        
        except Exception as e:
            return e

    def view_posted_item(self):

        db = self.connect_to_database()
        
        print(db['posts'].list_indexes())
        pass

    def dev_delete_items():
        pass

if __name__ == "__main__":
    pass
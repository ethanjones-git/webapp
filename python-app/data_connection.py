from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
from dotenv import load_dotenv

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


if __name__ == "__main__":

    # class class
    bs = BlobStorage()

    # parameters
    video_name = 'test_5.mp4'
    path =   os.getcwd()+"/data/output.mp4"

    bs.data_push(name=video_name,
                 path=path)
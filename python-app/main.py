
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from playwright.sync_api import sync_playwright
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from scrapper import screenshot
import os
import gridfs
from bson.binary import Binary
from data_connection import VideoBlob


class Main:
    def __init__(self):
        pass

    def connect_to_database(self):

        uri = "mongodb+srv://super_user:Z17DwuaZlwCAxOPH@dogbeachwebapp.dc02mag.mongodb.net/?retryWrites=true&w=majority&appName=dogbeachwebapp"

        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))

        # Ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            
                
        except Exception as e:
            print(e)

        db = client.dogbeachwebapp

        # Return connection
        return db

    def post_items(self):

        # Connect to database
        db = self.connect_to_database()

        try:

            # post this information
            post = {
                    "author": "Ethan",
                    "text": "Test post",
                    "tags": ["mongodb", "python", "pymongo"],
                    "date": datetime.datetime.now(tz=datetime.timezone.utc),
                }
            
            posts = db.posts
            post_id = posts.insert_one(post).inserted_id
            
            return "Post was successful"
        
        except Exception as e:
            return e

    def post_img(self, from_location,image_name):

        db = self.connect_to_database()

        with open(from_location + "/" + image_name, "rb") as f:
            binary_data = Binary(f.read())

        try:
            post = {
                "name":image_name,
                "image":binary_data,
                "date": datetime.datetime.now(tz=datetime.timezone.utc)
            }

            posts = db.posts
            post_id = posts.insert_one(post).inserted_id

            return post_id
        
        except Exception as e:
            return e

    def view_posted_item(self):

        db = self.connect_to_database()
        
        #print(db.list_collection_names())
        print(db['posts'].list_indexes())

    def dev_delete_items():
        '''
        
        #db = client.dogbeachwebapp
        #print(client.list_database_names())
        #print(client['dogbeachwebapp'].list_collection_names())

        try:

            myquery = {"author": "Ethan"}

            client['dogbeachwebapp']['posts'].delete_one(myquery)
        
        except:
            print("Fail")
        '''
        pass


if __name__ == "__main__":

    container_name = 'videos'
    input_data_path = os.getcwd() + '/data/output.mp4'

    vb = VideoBlob(container_name=container_name, 
                   input_data_path = input_data_path)

    vb.push_data('test_2.mp4')

#from_location = os.getcwd() + '/data'

#add_img(from_location,out+'_image.jpg')
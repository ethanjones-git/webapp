import datetime
import os
from video_recorder import VideoRecorder
import uuid
from dotenv import load_dotenv
from data_connection import MongoConnection, BlobStorage
from pathlib import Path

class RecordExportDelete:
    
    def __init__(self, video_length, stream_link):

        self.video_length = video_length

        self.stream_link = stream_link

        pass

    def record_export(self,id):

        export_name = f"{id}_video.mp4"

        vr  = VideoRecorder(mins_interval=self.video_length,
                                stream_link= self.stream_link,
                                export_name='data/'+export_name)
            
        out = vr.record_video()
        print(out)
    
    def mongo_export(self,id):

        try:

            # mongo connection
            try:
                mongo_connection = MongoConnection()
            
            except Exception as e:
                return f"Failed at mongo connection: {e}"
            
            # mongo push
            try:
                mongo_connection.video_meta_data(id=id)
            
            except Exception as e:
                return f"Failed at mongo push: {e}"
            
            return f"Mongo sucess at: {datetime.datetime.now()}"
        
        except Exception as e:
            return f"Mongo Error: {e}"
        
    def blob_export(self,id):

        try:

            # blob push
            bs = BlobStorage()
            bs.data_push(name=f'{id}_video.mp4',
                    path=os.getcwd()+f'/data'+ f'/{id}_video.mp4')
            
            return f"Blob export success at:{datetime.datetime.now()}"
        
        except Exception as e:
            return f"Error: {e}"
    
    def internal_delete(self,id):

        try:

            file=Path(os.getcwd()+f'/data'+ f'/{id}_video.mp4')
            file.unlink()

            return f"delete successful at:{datetime.datetime.now()}"
        
        except Exception as e:
            return f"Delete failed: {e}"
        
def execute_red_procedure(total_video_length, video_length, stream_link):
    
    # class
    red = RecordExportDelete(video_length, stream_link)

    # time when loop terminates
    future_utc = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=total_video_length)

     # while current is less than future time
    while datetime.datetime.now(tz=datetime.timezone.utc) < future_utc:
     
        try:
            # unique id
            id = str(uuid.uuid4())

            # record export
            out = red.record_export(id=id)
            print(out)

            # meta data export
            out = red.mongo_export(id=id)
            print(out)

            # blob export
            out = red.blob_export(id=id)
            print(out)

            # internal delete
            out = red.internal_delete(id=id)
            print(out)


        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    
    execute_red_procedure(total_video_length = 5,
                          video_length = 1,
                          stream_link = "https://www.youtube.com/watch?v=x10vL6_47Dw")


import subprocess
import time
import datetime
import uuid

'''
Run for 5 mins, export video and run. 
'''


class VideoRecorder:

    def __init__(self, mins_interval, stream_link, export_name):

        # convert mins to seconds
        self.secs = mins_interval*60

        # stream link commang
        self.streamlink_command = [
            "streamlink",
            #"https://www.youtube.com/watch?v=x10vL6_47Dw",
            stream_link,
            "best",
            "-o", 
            export_name
        ]

    
    def record_video(self):

        #dte = datetime.datetime.now(tz=datetime.timezone.utc)
        
        proc = subprocess.Popen(self.streamlink_command)
        #return "sub process timed out"

        time.sleep(self.secs)

        proc.terminate()  # or proc.kill()
        proc.wait()

        return id

        #end_dte = dte.strftime("%%H_%M_%S")
        #dte_time = str_dte + "_" + end_dte

if __name__ == '__main__':

    count = 1
    while count < 5:

        mins_interval = 1

        stream_link = "https://www.youtube.com/watch?v=x10vL6_47Dw"

        export_name = f"test_{count}"

        vr  = VideoRecorder(mins_interval=mins_interval,
                            stream_link=stream_link,
                            export_name=export_name)
        
        out = vr.record_video()
        print(out)
        print(f"Count is: {count}")
        count += 1
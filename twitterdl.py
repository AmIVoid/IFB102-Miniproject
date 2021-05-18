import os
import subprocess
from datetime import datetime
from st_management import manageFiles
from webhook import sendMessage

def twDownload(url):
    subprocess.run(['twitter-dl', '--tweet', '--video', './downloaded_videos', url])
    
twDownload('https://twitter.com/h31202123/status/1393514508627300354?s=19')
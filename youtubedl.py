import youtube_dl
import os
from datetime import datetime
from youtube_dl.YoutubeDL import YoutubeDL
from st_management import manageFiles

def download(url, quality):

    if quality == '360p':
        ydl_opts = {
            'format': '18',
            'outtmpl': 'downloaded_videos/%(title)s.%(ext)s'
        }
    elif quality == '480p':
        ydl_opts = {
            'format': '135',
            'outtmpl': 'downloaded_videos/%(title)s.%(ext)s'
        }
    elif quality == '720p':
        ydl_opts = {
            'format': '136',
            'outtmpl': 'downloaded_videos/%(title)s.%(ext)s'
        }
    elif quality == '1080p':
        ydl_opts = {
            'format': '137',
            'outtmpl': 'downloaded_videos/%(title)s.%(ext)s'
        }
    else: 
        ydl_opts = {
            'format': '18',
            'outtmpl': 'downloaded_videos/%(title)s.%(ext)s'
        }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        if os.path.isfile('logs/video_log.txt'):
            log = open('logs/video_log.txt', 'a')
            log.write(f'{datetime.now()} \'{filename}\'\n')
            log.close()
        else:
            log = open('logs/video_log.txt', 'w+')
            log.write(f'{datetime.now()} \'{filename}\'\n')
            log.close()
        manageFiles(r'.\downloaded_videos')
        return filename
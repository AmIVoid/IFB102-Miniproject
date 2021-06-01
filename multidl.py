import youtube_dl
import os
from datetime import datetime
from youtube_dl.YoutubeDL import YoutubeDL
from youtube_dl.utils import ytdl_is_updateable
from st_management import manageFiles
from webhook import sendMessage

def Download(url):
    ydl_opts = {
        'outtmpl': 'downloaded_videos/%(title)s.%(ext)s'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        title = info.get('title', None)
        sendMessage(f'**{title}** was just downloaded from YouTube.')
        if os.path.isfile('logs/video_log.txt'):
            log = open('logs/video_log.txt', 'a', encoding='utf-8')
            log.write(f'\n{datetime.now()} \'{filename}\'')
            log.close()
        else:
            log = open('logs/video_log.txt', 'w+', encoding='utf-8')
            log.write(f'{datetime.now()} \'{filename}\'')
            log.close()
        manageFiles(r'./downloaded_videos')
        return filename


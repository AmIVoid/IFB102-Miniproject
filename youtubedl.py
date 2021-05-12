import youtube_dl
from youtube_dl.YoutubeDL import YoutubeDL

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
        #ydl.download([url])
        filename = ydl.prepare_filename(info)
        return filename
from os import getenv
from dotenv import load_dotenv
import yt_dlp

load_dotenv()
PATH = getenv("SAVE_PATH")

def upload(url):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': f'{PATH}/%(title)s.%(ext)s',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            info_dict = ydl.extract_info(url, download=True)
            video_filename = ydl.prepare_filename(info_dict)
            
        return video_filename
    except Exception as e:
        raise e
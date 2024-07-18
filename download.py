import yt_dlp
import conf

def upload(url):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': f'{conf.SAVE_PATH}/%(title)s.%(ext)s',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            info_dict = ydl.extract_info(url, download=True)
            video_filename = ydl.prepare_filename(info_dict)
            
        return video_filename
    except Exception as e:
        raise e
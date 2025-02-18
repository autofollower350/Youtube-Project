# downloader.py
from pytube import YouTube
import os

def download_video(link, save_path='./downloads'):
    try:
        yt = YouTube(link)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
        
        # Ensure the download folder exists
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        
        # Download the video
        stream.download(output_path=save_path)
        print("Download complete!")
        return True
    except Exception as e:
        print(f"Error downloading video: {e}")
        return False
"""
Allows the user to download any youtube video to any file path.
"""

from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    """
    Downloads the YouTube video with url to the save_path.
    """
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive = True, file_extension = "mp4")
        highest_resolution = streams.get_highest_resolution()
        highest_resolution.download(output_path = save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

def open_file_dialog():
    """
    Opens the file_dialog box to allow file selection.
    """
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    
    return folder


#starts program
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube url: ")
    sav_dir = open_file_dialog()

    if not sav_dir:
        print("Invalid save location.")
    else:
        download_video(video_url,sav_dir)

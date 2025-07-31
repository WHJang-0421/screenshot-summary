import os
from moviepy import VideoFileClip

from src.disk_cache import get_cropped_video_path

def lower_third(video_path):
    clip = VideoFileClip(video_path)
    w,h = clip.size
    return {
        "x1": 0,
        "y1": h*(2/3),
        "x2": w,
        "y2": h
    }

def crop_and_save(video_path, x1, y1, x2, y2):
    cropped_video_path = get_cropped_video_path(video_path, x1, y1, x2, y2)
    if (os.path.exists(cropped_video_path)):
        return
    clip = VideoFileClip(video_path)
    cropped = clip.cropped(x1=x1, y1=y1, x2=x2, y2=y2)
    cropped.write_videofile(cropped_video_path)

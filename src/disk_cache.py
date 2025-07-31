import os
import pickle
from scenedetect import detect

def get_cache_path(video_path):
    video_name = os.path.basename(video_path) 
    cache_dir = ".cache"
    cache_name = os.path.splitext(video_name)[0] + ".pkl"
    return os.path.join(cache_dir, cache_name)

def get_image_path(video_path, seconds, postfix=""):
    video_name = os.path.basename(video_path) 
    image_dir = "out"
    return os.path.join(image_dir, os.path.splitext(video_name)[0] + f"_{ postfix }", f"{seconds}s.jpg")

def get_cropped_video_path(video_path, x1, y1, x2, y2):
    video_name = os.path.basename(video_path) 
    cropped_dir = "cropped"
    return os.path.join(cropped_dir, os.path.splitext(video_name)[0] + f"_{x1}_{y1}_{x2}_{y2}.mp4")

def detect_with_cache(video_path, *args, **kwargs):
    '''
    Enhances detect with caching. expects the cache file to be named exactly the same as the video file, except for the extension.
    '''
    # TODO fix caching issue: same cache file for different detectors
    cache_path = get_cache_path(video_path)

    if os.path.exists(cache_path):
        with open(cache_path, "rb") as file:
            return pickle.load(file)

    result = detect(video_path, *args, **kwargs)
    with open(cache_path, "wb") as file:
        pickle.dump(result, file)
    return result

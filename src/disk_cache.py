import os
import pickle
from scenedetect import detect

def get_cache_path(video_path):
    video_name = os.path.basename(video_path) 
    cache_dir = ".cache"
    cache_name = os.path.splitext(video_name)[0] + ".pkl"
    return os.path.join(cache_dir, cache_name)

def get_image_path(video_path, seconds):
    video_name = os.path.basename(video_path) 
    image_dir = "out"
    cache_name = os.path.splitext(video_name)[0] + f"{seconds}s" + ".jpg"
    return os.path.join(image_dir, cache_name)

def detect_with_cache(video_path, *args, **kwargs):
    '''
    Enhances detect with caching. expects the cache file to be named exactly the same as the video file, except for the extension.
    '''
    cache_path = get_cache_path(video_path)

    if os.path.exists(cache_path):
        with open(cache_path, "rb") as file:
            return pickle.load(file)

    result = detect(video_path, *args, **kwargs)
    with open(cache_path, "wb") as file:
        pickle.dump(result, file)
    return result

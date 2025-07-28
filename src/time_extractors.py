from scenedetect import ContentDetector, AdaptiveDetector
from src.disk_cache import detect_with_cache

def middle_of(scene):
    start, end = scene
    start_time = start.get_seconds()
    end_time = end.get_seconds()
    middle = (start_time + end_time) / 2
    return round(middle, 3)

def extract_time_from_detector(video_path, detector):
    scene_list = detect_with_cache(video_path, detector)

    screenshot_times = []
    for scene in scene_list:
        screenshot_times.append(middle_of(scene))

    return screenshot_times

from scenedetect import ContentDetector
from video_extractor import VideoFrameExtractor
from disk_cache import detect_with_cache

video_path = "resources/video1.mp4"
scene_list = detect_with_cache(video_path, ContentDetector())

screenshot_times = []
for start, end in scene_list:
    start_time = start.get_seconds()
    end_time = end.get_seconds()
    middle = (start_time + end_time) / 2
    screenshot_times.append(middle)

with VideoFrameExtractor(video_path) as extractor:
    for i, t in enumerate(screenshot_times):
        img = extractor.extract_and_save(30)

# for future refactoring
class ContentTimeSampler:
    pass

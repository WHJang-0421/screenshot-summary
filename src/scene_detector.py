from scenedetect import detect, ContentDetector
from video_extractor import VideoFrameExtractor

video_path = "resources/[ENG_SUB] 일론 머스크의 창당, 미국에서 제3당이 성공할 수 있을까_ _ 양당제, 민주당, 공화당.mp4"
scene_list = detect(video_path, ContentDetector())

screenshot_times = []
for start, end in scene_list:
    start_time = start.get_seconds()
    end_time = end.get_seconds()
    middle = (start_time + end_time) / 2
    screenshot_times.append(middle)

with VideoFrameExtractor(video_path) as extractor:
    for i, t in enumerate(screenshot_times):
        img = extractor.extract_image(t)
        extractor.save(img, f"out/content_detector/{i}.jpg")
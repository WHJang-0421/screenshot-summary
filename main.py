from scenedetect import ContentDetector
from src.video_extractor import VideoFrameExtractor
from src.time_extractors import extract_time_from_detector

def main():
    video_path = "resources/video1.mp4"
    extract_times = extract_time_from_detector(video_path, ContentDetector())

    # TODO use more advanced strategies for time extraction

    with VideoFrameExtractor(video_path) as extractor:
        for t in extract_times:
            extractor.extract_and_save(t, postfix="content_detector")


if __name__ == "__main__":
    main()

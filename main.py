from scenedetect import ContentDetector #, AdaptiveDetector # seems like the type of detector doesn't make a big difference
from src.video_extractor import VideoFrameExtractor
from src.time_extractors import extract_time_from_detector

def main():
    video_path = "resources/video1.mp4"

    detector = ContentDetector()
    detector_name = "content_detector"

    extract_times = extract_time_from_detector(video_path, detector)

    # TODO use more advanced strategies for time extraction

    with VideoFrameExtractor(video_path) as extractor:
        for t in extract_times:
            extractor.extract_and_save(t, postfix=detector_name) 


if __name__ == "__main__":
    main()

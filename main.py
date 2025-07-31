from scenedetect import ContentDetector , AdaptiveDetector # seems like the type of detector doesn't make a big difference
from src.disk_cache import get_cropped_video_path
from src.video_cropping import crop_and_save, lower_third
from src.video_extractor import VideoFrameExtractor
from src.time_extractors import extract_time_from_detector

def main():
    video_path = "resources/video1.mp4"

    # crop video
    crop_coordinates = lower_third(video_path)
    crop_and_save(video_path, **crop_coordinates)
    cropped_video_path = get_cropped_video_path(video_path, **crop_coordinates)


    # extract the crop times
    detector = AdaptiveDetector(min_content_val=5)
    detector_name = "adaptive_detector_with_cropping"
    extract_times = extract_time_from_detector(cropped_video_path, detector)

    # take screenshots
    with VideoFrameExtractor(video_path) as extractor:
        for t in extract_times:
            extractor.extract_and_save(t, postfix=detector_name) 


if __name__ == "__main__":
    main()

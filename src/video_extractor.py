import os
from moviepy import VideoFileClip
from PIL import Image
from src.disk_cache import get_image_path

class VideoFrameExtractor:
    def __init__(self, video_path):
        self.video_path = video_path
        self.clip = None


    def __enter__(self):
        self.clip = VideoFileClip(self.video_path)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.clip:
            self.clip.close()

    def extract_and_save(self, second, override=False, postfix=""):
        image_path = get_image_path(self.video_path, second, postfix)
        if not override and os.path.exists(image_path):
            return

        image_folder = os.path.dirname(image_path)
        os.makedirs(image_folder, exist_ok=True)

        frame = self.clip.get_frame(second)
        img = Image.fromarray(frame)
        img.save(image_path)
        return img
    
if __name__ == "__main__":
    with VideoFrameExtractor("resources/video1.mp4") as extractor:
        img = extractor.extract_and_save(30)

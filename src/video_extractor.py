from moviepy import VideoFileClip
from PIL import Image

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

    def extract_image(self, second):
        frame = self.clip.get_frame(second)
        img = Image.fromarray(frame)
        return img
    
    @staticmethod
    def save(image, path):
        image.save(path)

if __name__ == "__main__":
    with VideoFrameExtractor("resources/[ENG_SUB] 일론 머스크의 창당, 미국에서 제3당이 성공할 수 있을까_ _ 양당제, 민주당, 공화당.mp4") as extractor:
        img = extractor.extract_image(30)
        extractor.save(img, "out/screenshot30s.jpg")
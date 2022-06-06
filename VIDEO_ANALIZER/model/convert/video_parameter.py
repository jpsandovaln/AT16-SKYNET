class VideoParameter:
    def __init__(self):
        self.ffmpeg_path = ''
        self.video_path = ''
        self.output_folder = ''

    def get_ffmpeg_path(self):
        return self.ffmpeg_path

    def set_ffmpeg_path(self, ffmpeg):
        self.ffmpeg_path = ffmpeg

    def get_video_path(self):
        return self.video_path

    def set_video_path(self, video_path):
        self.video_path = video_path

    def get_output_folder(self):
        return self.output_folder

    def set_output_folder(self, output_folder):
        self.output_folder = output_folder

    def validate(self):
        if self.output_folder is None or self.video_path is None or self.ffmpeg_path is None:
            raise TypeError

        if not self.output_folder or not self.video_path or not self.ffmpeg_path:
            raise TypeError

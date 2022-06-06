class VideoCommand:
    def __init__(self):
        self.input = '-i'
        self.frame_rate_ps = 'fps=1'
        self.video_f = '-vf'
        self.image_name = '%d.jpg'

    def build(self, video_parameter):
        cmd = [
            video_parameter.get_ffmpeg_path(),
            self.input,
            video_parameter.get_video_path(),
            self.video_f,
            self.frame_rate_ps,
            video_parameter.get_output_folder() + self.image_name
        ]
        return cmd

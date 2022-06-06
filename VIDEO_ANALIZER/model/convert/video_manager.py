from model.convert.video_command import VideoCommand
from model.convert.executer import Executer


class VideoManger:
    def convert(self, video_parameter):
        video_parameter.validate()
        video_command = VideoCommand()
        cmd = video_command.build(video_parameter)
        ex = Executer()
        ex.execute(cmd)

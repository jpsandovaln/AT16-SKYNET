# 
# @convert_audio.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
# 
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from src.model.convertor import Convertor
import subprocess


class ConvertAudio(Convertor):

    # Constructor input, input data, input file
    def __init__(self, input_data: any, input_file: any):
        super().__init__(input_data, input_file)
        self.instructions: str = self.get_instructions()

    # Method to compare the data
    def init_dic(self) -> dict:
        dic_param: dict = {'bitrate': 'ab {}k ',
                           'sample-rate': 'ar {} ',
                           'audio-channel': 'ac {} '}
        return dic_param

    # Method to create the ffmpeg command.
    def concatenate(self) -> str:
        dic: dict = self.init_dic()
        cmd_input: str = "-"
        for key in dic:
            val: any = self.instructions.values.get(key)
            if len(val) > 0:
                cmd_input += dic[key].format(val) + '-'
        cmd_input_copy: str = cmd_input[:-1]

        return cmd_input_copy

    # Method to converter the visual content.
    def exec(self) -> bool:
        concatenate: str = self.concatenate()
        try:
            direction: str = self.output_file + r'/' + self.name_output
            ffmpeg_command: str = "ffmpeg -i {}  {} {}".format(self.input_file, concatenate, direction)
            subprocess.call(ffmpeg_command)
            return True
        except:
            return False

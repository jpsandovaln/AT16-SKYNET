# 
# @object_result.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
# 
# This software is the confidential and proprietary information of
# Jalasoft, ("Condidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import os

from CONVERT_SERVICES.src.model.convertor import Convertor
import subprocess


class ConvertAudio(Convertor):

    def __init__(self, input_data, input_file):
        super().__init__(input_data, input_file)
        self.instructions = self.getInstructions()

    def Init_dic(self):
        dic_param = {'acodex': 'c:a {} ',
                     'bitrate': 'ab {}k ',
                     'sambple-rate': 'ar {} ',
                     'audio-channel': 'ac {} '}
        return dic_param

    def Concatenate(self):
        dic = self.Init_dic()
        cmd_input = "-"
        for key in dic:
            val = self.instructions.values.get(key)
            if len(val) > 0:
                cmd_input += dic[key].format(val) + '-'
        cmd_input_copy = cmd_input[:-1]
        return cmd_input_copy

    def Exec(self):
        concatenate = self.Concatenate()
        try:
            dir = self.output_file + r'/' + self.name_output
            ffmpeg_command = "ffmpeg -i {}  {} {}".format(self.input_file, concatenate, dir )
            subprocess.call(ffmpeg_command)
            return True
        except:
            return False
#
# @ConvertAudio.py Copyright (c)
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

from params import Params


# This class inherits the inputs of the converter and converter visual content.
class ConvertAudio(Params):
    def __init__(self, str_input, path_out, path_in):
        super().__init__(str_input, path_out, path_in)
        self.dictionary = Params.dic_str_input(self)
        self.cmd_input_copy = self.compare_dic()
        self.ffmpeg_cmd = self.cmd_ff()

# This method compare the data and create the ffmpeg command.
    def compare_dic(self):
        dic_param = {'acodex': 'c:a {}',
                     'bitrate': 'ab {}k ',
                     'sambple-rate': 'ar {} ',
                     'audio-channel': 'ac {} '}
        cmd_input = "-"
        for key, val in self.dictionary.items():
            if key in dic_param:
                cmd_input += dic_param[key].format(val) + '-'
        cmd_input_copy = cmd_input[:-1]
        return cmd_input_copy

# This method converter the visual content.
    def cmd_ff(self):
        form_conv = ""
        for key, val in self.dictionary.items():
            if key == 'format':
                form_conv = val
        try:
            ffmpeg_command = "ffmpeg -i {}  {} {}\Converted_Audio.{}".\
                format(self.path_in, self.cmd_input_copy, self.path_out,
                       form_conv)

            import subprocess
            subprocess.call(ffmpeg_command)
            return True
        except:
            return False


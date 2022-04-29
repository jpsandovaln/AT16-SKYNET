# 
# @convert_video.py Copyright (c)
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

from src.model.convertor import Convertor
import os
import subprocess
import shutil


class ConvertVideo(Convertor):
    def __init__(self, input_data, input_file):
        super().__init__(input_data, input_file)
        self.instructions = self.get_instructions()

    # This method compare the data and create the ffmpeg command.
    def init_dic(self):
        dic_param = {'frame': 'fps={}',
                     'width': '{}/1:',
                     'height': '{}/2',
                     'color': 'format=gray'}
        return dic_param

    # Method to create the ffmpeg command.
    def concatenate(self):
        dic = self.init_dic()
        cmd_input = ""
        for key in dic:
            val = self.instructions.values.get(key)
            if len(val) > 0:
                if key == 'width':
                    cmd_input += 'scale=' + dic[key].format(val)
                cmd_input += dic[key].format(val) + ','
        cmd_input_copy = cmd_input[:-1]
        return cmd_input_copy

    # This method converter the visual content.
    def exec(self):
        concatenate = self.concatenate()
        try:
            name = self.name_output.split('.')
            output_file = self.output_file + '/' + name[0]
            os.mkdir(output_file)
            name_dir = output_file + '/' + name[0] + '%d.' + name[1]
            ffmpeg_command = "ffmpeg -i {} -vf {} {}".format(self.input_file, concatenate, name_dir)
            subprocess.call(ffmpeg_command)
            shutil.make_archive(output_file, 'zip', output_file)
            self.set_name_output(name[0] + '.zip')
            shutil.rmtree(output_file)
            return True
        except:
            return False

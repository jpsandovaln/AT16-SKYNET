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
import shutil


class ConvertVideo(Convertor):
    def __init__(self, input_data, input_file):
        super().__init__(input_data, input_file)
        self.instructions = self.getInstructions()

    # This method compare the data and create the ffmpeg command.
    def Init_dic(self):
        dic_param = {'frame': 'fps={}',
                     'widht': '{}/1:',
                     'height': '{}/2',
                     'color': 'format=gray'}
        return dic_param

    def Concatenate(self):
        dic = self.Init_dic()
        cmd_input = ""
        for key in dic:
            val = self.instructions.values.get(key)
            if len(val) > 0:
                if key == 'widht':
                    print(val)
                    cmd_input += 'scale=' + dic[key].format(val)
                elif key in dic:
                    cmd_input += dic[key].format(val) + ','
        cmd_input_copy = cmd_input[:-1]
        return cmd_input_copy

    #This method converter the visual content.
    def Exec(self):
        concatenate = self.Concatenate()
        try:
            name = self.name_output.split('.')
            output_file = self.output_file + '/' + name[0]
            os.mkdir(output_file)
            name_dir = output_file + '/' + name[0] + '%d.' + name[1]
            ffmpeg_command = "ffmpeg -i {} -vf {} {}".format(self.input_file, concatenate, name_dir)
            subprocess.call(ffmpeg_command)
            shutil.make_archive(output_file, 'zip', output_file)
            self.setNameOutput(name[0] + '.zip')
            shutil.rmtree(output_file)
            return True
        except:
            return False
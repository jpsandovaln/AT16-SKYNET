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

from CONVERT_SERVICES.src.model.convertor import Convertor
import os


class ConvertImage(Convertor):

    #  constructor   instruciones folder formato folder_salida
    def __init__(self, input_data, input_file):
        super().__init__(input_data, input_file)
        self.instructions = self.getInstructions()

    def Init_dic(self):
        dic_param = {'color': ' -colorspace {} ',
                     'rotate': ' -rotate {} ',
                     'mirrorvert': ' -flip ',
                     'mirrorhori': ' -flop ',
                     'widht': ' -resize {}',
                     'height': 'x{}! '}
        return dic_param

    def Concatenate(self):
        dic = self.Init_dic()
        cod_cmd = "magick convert " + self.input_file + " "
        for key in dic:
            val = self.instructions.values.get(key)
            if len(val) > 0:
                dic[key] = dic[key].format(val)
                cod_cmd += dic[key]
        cod_cmd += self.output_file + '/' + self.name_output
        return cod_cmd

    def Exec(self):
        cod_cmd = self.Concatenate()
        os.system(cod_cmd)
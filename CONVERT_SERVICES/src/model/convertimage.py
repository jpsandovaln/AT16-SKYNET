#
# @object_result.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
#1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
#All rights reserved.
#
#This software is the confidential and proprietary information of
#Jalasoft, ("Condidential Information"). You shall # not
#disclose such Confidential Information and shall use it only in
#accordance with the terms of the license agreement you entered into
#with Jalasoft.
#

from src.convert.convertor import Convertor
import os


class ConvertImage(Convertor):

    def __init__(self, input_data, input_file, output_file, out_format):
        super().__init__(input_file, output_file, out_format, input_data)
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
        cod_cmd = "magick converter " + self.inputfile + " "
        for key, val in self.instructions.items():
            if key in dic:
                dic[key] = dic[key].format(val)
                cod_cmd += dic[key]
        cod_cmd += self.outputfile + '\output12.'+self.format
        return cod_cmd

    def Exec(self):
        cod_cmd = self.Concatenate()
        os.system(cod_cmd)

"""  def Execute(self):
        self.Verify()
        #cod = 'magick converter {} -colorspace {}{}{}{}{} '.format()
        print (self.instructions)

    def Verify(self):
        self.instructions = self.instructions.split(sep=',')
        for i in range(len(self.instructions)):
           self.instructions[i] = self.instructions[i].strip().lower()
        #verify color
        val = self.instructions[0]
        if (val != 'sRGB') and (val != 'gray') and (val != 'sRGB'):
            self.instructions[0] = 'sRGB'
        #verify horizontal mirror
        if self.instructions[-1] == 'true':
            self.instructions[-1] = '-flip'
        else:
            self.instructions[-1] = ''
        # verify vertical mirror
        if self.instructions[-2] == 'true':
            self.instructions[-2] = '-flop'
        else:
            self.instructions[-2] =  '
        """

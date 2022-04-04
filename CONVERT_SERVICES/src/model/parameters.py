#
# @video_converter.py Copyright (c)
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

from model1.converter import Converter


#This class inherits the inputs of the converter.
class Parameters(Converter):
    def __init__(self, str_input, path_out, path_in):
        super().__init__(str_input, path_out, path_in)
        self.spl_str_input = str_input.split(',')
        self.dictionary = self.dic_str_input()

    #This method creates a dictionary of the input parameters.
    def dic_str_input(self):
        dictionary = {}
        for k_v in self.spl_str_input:
            if '=' in k_v:
                k_v = k_v.split('=')
                dictionary[(k_v[0]).strip().lower()] = (k_v[1])
            else:
                dictionary[(k_v[:]).strip().lower()] = ''
        return dictionary




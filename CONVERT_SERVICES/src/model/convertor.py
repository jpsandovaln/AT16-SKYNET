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
#with Jalasoft .
#

from src.convert.parameters import Parameters

class Convertor(Parameters):
    def __init__(self, input_file, output_file, outformat, instructions):
        super().__init__(instructions)
        self.inputfile = input_file
        self.outputfile = output_file
        self.format = outformat
        self.instructions = self.dic_str_input()

    def getInputFile(self):
        return self.inputfile

    def getOutFile(self):
        return self.outputfile

    def getFormat(self):
        return self.format

    def getInstructions(self):
        return self.instructions


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
# with Jalasoft .
#

class Convertor:
    #  constructor  instruciones folder
    def __init__(self, instructions, folder):
        name = instructions.files['file'].filename
        self.input_file = folder+'/' + name
        self.output_file = r'saved_files/' + (instructions.values.get('Convert')).lower() + '_download'
        name = name.split('.')
        self.format = instructions.values.get('format')
        self.name_output = name[0] + 'new.' + self.format
        self.instructions = instructions

    def getInputFile(self):
        return self.inputfile

    def getOutFile(self):
        return self.outputfile

    def getFormat(self):
        return self.format

    def getInstructions(self):
        return self.instructions

    def setNameOutput(self, val):
        self.name_output = val


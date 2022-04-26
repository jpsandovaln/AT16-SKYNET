#
# @convertor.py Copyright (c)
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
        self.output_file = r'saved_files/' + (instructions.values.get('convert')).lower() + '_download'
        name = name.split('.')
        self.format = instructions.values.get('format')
        self.name_output = name[0] + 'new.' + self.format
        self.instructions = instructions

    def get_input_file(self):
        return self.inputfile

    def get_out_file(self):
        return self.outputfile

    def get_format(self):
        return self.format

    def get_instructions(self):
        return self.instructions

    def set_name_output(self, val):
        self.name_output = val


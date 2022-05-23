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

from src.model.parameters import Parameters


class Convertor:
    #  Constructor parent for all convertors, inputs: instructions, folder
    def __init__(self, instructions: str, folder: str):
        name: str = instructions.files['file'].filename
        self.input_file: str = folder + '/' + name
        param: Parameters = Parameters(folder, instructions)
        param.validate_get_convert()
        # param.validate_in_format()
        self.output_file: str = r'saved_files/' + (
            instructions.values.get('convert')).lower() + '_download'
        name: any = name.split('.')
        param.validate_format()
        self.format: str = instructions.values.get('format')
        self.name_output: str = name[0] + 'new.' + self.format
        self.instructions: str = instructions
        print(name, 'es nombre', param, 'es parametros')

    def get_input_file(self) -> str:
        return self.input_file

    def get_out_file(self) -> str:
        return self.output_file

    def get_format(self) -> str:
        return self.format

    def get_instructions(self) -> str:
        return self.instructions

    def set_name_output(self, output_name: str):
        self.name_output: str = output_name

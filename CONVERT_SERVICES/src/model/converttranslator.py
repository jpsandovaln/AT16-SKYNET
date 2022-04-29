#
# @Main_SR.py Copyright (c) 2022 Jalasoft
# 2643 Av Melchor Perez de Olguin , Colquiri Sud, Cochabamba, Bolivia.
# add direccion de jala la paz>
# All rights reserved
#
# This software is the confidential and proprietary information of
# Jalasoft , Confidential Information "). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft


from deep_translator import GoogleTranslator
from src.model.convertor import Convertor


class ConvertTranslator(Convertor):
    def __init__(self, input_data, input_file):
        super().__init__(input_data, input_file)
        self.path = input_file  # input folder
        self.file = input_data.files['file'].filename
        self.instructions = self.getInstructions()
        self.language_in = self.instructions.values.get('language_in')
        self.language_out = self.instructions.values.get('language_out')

    # define function for extract metadata
    def exec(self):
        language_in = self.language_in.split('-')
        language_out = self.language_out.split('-')
        translator = GoogleTranslator(source=language_in[0], target=language_out[0])
        file = open(self.input_file, mode='r')
        texto = file.read()
        result = translator.translate(texto)
        with open(self.output_file + '/' + self.name_output, mode='w') as file:
            file.write(result)

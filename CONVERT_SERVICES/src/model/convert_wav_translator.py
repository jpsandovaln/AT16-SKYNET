#
# @convert_wav_to_txt.py Copyright (c) 2022 Jalasoft
# 2643 Av Melchor Perez de Olguin , Colquiri Sud, Cochabamba, Bolivia.
# add direccion de jala la paz>
# All rights reserved
#
# This software is the confidential and proprietary information of
# Jalasoft , Confidential Information "). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft

import speech_recognition as sr
from src.model.convertor import Convertor
from src.model.convert_translator import ConvertTranslator
from src.model.convert_wav_to_txt import ConvertWavTxt


class ConvertWavTranslator(Convertor):
    # define the input of class
    def __init__(self, input_data: str, input_file: str):
        super().__init__(input_data, input_file)
        self.path: str = input_file  # input folder
        self.request: str = input_data

    # define function for extract metadata
    def exec(self):
        wav_translator: any = ConvertWavTxt(self.request, self.path)
        result: any = wav_translator.wav_text()
        translator: any = ConvertTranslator(self.request, self.path)
        result_finish: any = translator.translator_text(result)
        with open(self.output_file + '/' + self.name_output, mode='w') as file:
            file.write(result_finish)

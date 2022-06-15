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


class ConvertWavTxt(Convertor):
    # define the input of class
    def __init__(self, input_data: str, input_file: str):
        super().__init__(input_data, input_file)
        self.path: str = input_file  # input folder
        self.file: str = input_data.files['file'].filename
        self.instructions: str = self.get_instructions()
        self.language_in: str = self.instructions.values.get('language_in')

    def wav_text(self):
        r: any = sr.Recognizer()
        audio_file: any = sr.AudioFile(self.input_file)
        with audio_file as source:
            r.adjust_for_ambient_noise(source)
            sound: any = r.record(source)
            result: any = r.recognize_google(sound, language=self.language_in)
        return str(result)

    # define function for extract metadata
    def exec(self):
        result_finish = self.wav_text()
        with open(self.output_file + '/' + self.name_output, mode='w') as file:
            file.write(result_finish)



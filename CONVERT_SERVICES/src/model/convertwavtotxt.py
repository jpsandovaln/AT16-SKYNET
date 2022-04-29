#
# @convertwavtotxt.py Copyright (c) 2022 Jalasoft
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
    def __init__(self, input_data, input_file):
        super().__init__(input_data, input_file)
        self.path = input_file  # input folder
        self.file = input_data.files['file'].filename
        self.instructions = self.getInstructions()
        self.language_in = self.instructions.values.get('language_in')

    # define function for extract metadata
    def exec(self):
        r = sr.Recognizer()
        audio_file = sr.AudioFile(self.input_file)

        with audio_file as source:
            r.adjust_for_ambient_noise(source)
            sound = r.record(source)
            result = r.recognize_google(sound, language=self.language_in)

        with open(self.output_file + '/' + self.name_output, mode='w') as file:
            file.write(result)

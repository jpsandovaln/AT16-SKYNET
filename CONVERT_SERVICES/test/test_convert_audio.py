#
# test_convert_audio.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# Edificio Union № 1376 Av. General Inofuentes esquina Calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import unittest
from src.model.convert_audio import ConvertAudio


class TestConvertAudio(unittest.TestCase):

    def test_convert_audio(self):
        input_data = {'acodex': 'c:a {} ',
                     'bitrate': 'ab {}k ',
                     'sambple-rate': 'ar {} ',
                     'audio-channel': 'ac {} '}
        input_data =
        input_file = './saved_files/upload'
        convert = ConvertAudio()
        result = convert.exec()
        self.assertEqual()
        self.assertTrue()

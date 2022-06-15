#
# @test_convert_ocr.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import unittest
from src.model.convert_ocr import ConvertOCR


class TestConvertOCR(unittest.TestCase):

    def setUp(self):
        self.result = ConvertOCR.init_dic(self)
        self.example = {'acodex': 'c:a {} ',
                        'bitrate': 'ab {}k ',
                        'sambple-rate': 'ar {} ',
                        'audio-channel': 'ac {} '}
        self.example_str = ''
        self.example_void_array = {'', '', '', ''}

    def test_convert_audio(self):
        self.assertEqual(self.example, self.result, "return is equal")

    def test_convert_audio_str(self):
        self.assertNotEqual(self.example_str, self.result, "return is not equal")

    def test_convert_audio_number(self):
        self.assertNotEqual(self.example_void, self.result, "return is not equal")
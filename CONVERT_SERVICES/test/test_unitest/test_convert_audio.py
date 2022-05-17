#
# @test_convert_audio.py Copyright (c)
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
from src.model.convert_audio import ConvertAudio


class TestConvertAudio(unittest.TestCase):

    def setUp(self):
        self.result = ConvertAudio.init_dic(self)
        self.example = {'bitrate': 'ab {}k ',
                        'sample-rate': 'ar {} ',
                        'audio-channel': 'ac {} '}

        self.example_str = ''
        self.example_void = {'', '', '', ''}
        self.example_concatenate = {'bitrate': 'ab {}k ',
                                    'sample-rate': 'ar {} ',
                                    'audio-channel': 'ac {} ',
                                    'format': 'mp3'}

        self.example_str_concatenate = {'bitrate': 'ab {}k ',
                                        'sample-rate': 'ar {} ',
                                        'audio-channel': 'ac {} ',
                                        'format': 'mp2'}

        self.result_concatenate_format = {'bitrate': 'ab {}k ',
                                               'sample-rate': 'ar {} ',
                                               'audio-channel': 'ac {} ',
                                               'format': 'm4a'}

        self.result_concatenate_format_str = {'bitrate': 'ab {}k ',
                                               'sample-rate': 'ar {} ',
                                               'audio-channel': 'ac {} ',
                                               'format': 'wav'}

    def test_convert_audio(self):
        self.assertEqual(self.example, self.result, "return is equal")

    def test_convert_audio_str(self):
        self.assertNotEqual(self.example_str, self.result, "return is not equal a str")

    def test_convert_audio_number(self):
        self.assertNotEqual(self.example_void, self.result, "return is not equal a number")

    def test_convert_audio_concatenate(self):
        self.assertNotEqual(self.example_str_concatenate, self.result, "return is not equal concatenate")

    def test_convert_audio_format_concatenate(self):
        self.assertNotEqual(self.result_concatenate_format, self.result,
                            "return is not equal str concatenate ")

    def test_convert_audio_number_concatenate(self):
        self.assertNotEqual(self.result_concatenate_format_str, self.result,
                            "return is not equal format str")

#
# @test_convert_metadata.py Copyright (c)
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
from src.model.convert_metadata import ConvertMetadata


class TestConvertMetadata(unittest.TestCase):

    def setUp(self):
        self.result = ConvertMetadata.init_dic(self)
        self.example = {"third_party/win/Exiftool"}
        self.example_str = ''
        self.example_void = {'               '}

    def test_convert_audio(self):
        self.assertEqual(self.example, self.result, "return is equal")

    def test_convert_audio_str(self):
        self.assertNotEqual(self.example_str, self.result, "return is not equal")

    def test_convert_audio_number(self):
        self.assertNotEqual(self.example_void, self.result, "return is not equal")
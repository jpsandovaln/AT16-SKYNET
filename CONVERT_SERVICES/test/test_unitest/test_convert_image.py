#
# @test_convert_image.py Copyright (c)
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
from src.model.convert_image import ConvertImage


class TestConvertImage(unittest.TestCase):

    def setUp(self):
        self.result = ConvertImage.init_dic(self)
        self.example = {'color': ' -colorspace {} ',
                        'rotate': ' -rotate {} ',
                        'vertical_flip': ' -flip ',
                        'horizontal_flip': ' -flop ',
                        'width': ' -resize {}',
                        'height': 'x{}! '}
        self.example_str = ''
        self.example_void = {'', '', '', ''}
        self.example_formatone = {'color': ' -colorspace {} ',
                        'rotate': ' -rotate {} ',
                        'vertical_flip': ' -flip ',
                        'horizontal_flip': ' -flop ',
                        'width': ' -resize {}',
                        'height': 'x{}! ',
                        'format': 'jpg'}
        self.example_formattwo = {'color': ' -colorspace {} ',
                        'rotate': ' -rotate {} ',
                        'vertical_flip': ' -flip ',
                        'horizontal_flip': ' -flop ',
                        'width': ' -resize {}',
                        'height': 'x{}! ',
                        'format': 'png'}
        self.example_formatthree = {'color': ' -colorspace {} ',
                        'rotate': ' -rotate {} ',
                        'vertical_flip': ' -flip ',
                        'horizontal_flip': ' -flop ',
                        'width': ' -resize {}',
                        'height': 'x{}! ',
                        'format': 'webp'}

    def test_convert_image(self):
        self.assertEqual(self.example, self.result, "return is equal")

    def test_convert_image_str(self):
        self.assertNotEqual(self.example_str, self.result, "return is not equal")

    def test_convert_image_number(self):
        self.assertNotEqual(self.example_void, self.result, "return is not equal")

    def test_convert_image_void(self):
        self.assertNotEqual(self.example_formatone, self.result, "return is equal")

    def test_convert_image_str_format(self):
        self.assertNotEqual(self.example_formattwo, self.result, "return is not equal")

    def test_convert_image_format(self):
        self.assertNotEqual(self.example_formatthree, self.result, "return is not equal")
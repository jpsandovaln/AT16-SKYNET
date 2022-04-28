#
# test_convert_image.py Copyright (c) 2022 Jalasoft.
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
from src.model.convert_image import ConvertImage


class TestConvertImage(unittest.TestCase):
    def test_convert_image(self):
        input_data = {'files': r'',
                      'color': ' -colorspace sRGB ',
                      'rotate': ' -rotate 45 ',
                      'vertical_flip': ' -flip ',
                      'horizontal_flip': ' -flop ',
                      'width': ' -resize 1000',
                      'height': 'x1000! ',
                      'format': 'png'}
        input_file = './saved_files/upload'
        convert = ConvertImage(input_data, input_file)
        result = convert.concatenate()
        self.assertI.assertEqual(
            r'magick convert saved_files\upload/husky-t.jpg  -colorspace sRGB  -rotate 45  -flip  -flop  -resize 1000x1000! saved_files/image_download/husky-tnew.png',
            result)

    def test_convert_image(self):
        file = './saved_files/upload/2.jpg'
        input_file = './saved_files/upload'
        convert = ConvertImage(file, input_file)
        result = convert.concatenate()
        self.assertI.assertEqual(
            r'magick convert saved_files\upload/husky-t.jpg  -colorspace sRGB  -rotate 45  -flip  -flop  -resize 1000x1000! saved_files/image_download/2new.png',
            result)

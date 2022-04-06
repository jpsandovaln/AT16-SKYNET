#
# @Test.py Copyright (c)
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
from CONVERT_SERVICES.src.Convert_Audio.ConvertAudio import ConvertAudio


class Test_converter(unittest.TestCase):

    def test_tdd_conv_audio(self):
        cal = ConvertAudio('format=m4a, audio-channel=6, bitrate=40000, sambple-rate=24000, acodex=aac',
                            r'./CONVERT_SERVICES/test/input/OST.mp3',
                            r'./CONVERT_SERVICES/saved_files')
        self.assertTrue(cal)

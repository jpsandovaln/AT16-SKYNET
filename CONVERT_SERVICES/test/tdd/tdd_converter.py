#
# @video_converter.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
#1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
#All rights reserved.
#
#This software is the confidential and proprietary information of
#Jalasoft, ("Condidential Information"). You shall # not
#disclose such Confidential Information and shall use it only in
#accordance with the terms of the license agreement you entered into
#with Jalasoft.
#

import unittest
from model1.ffmpeg_conv import CommandFfmpeg

class Test_converter(unittest.TestCase):

    def test_tdd_conv_video_to_blackwhite_video(self):
        cal = CommandFfmpeg('frame=1, gray, format=png, widht=190, height=200',
                        r'C:\Users\rodri\Desktop\videos\video2.mp4',
                        r'C:\Users\rodri\Desktop\py4e\frames')
        self.assertTrue(cal)




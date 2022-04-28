#
# @load_image_train.py Copyright (c) 2022 Jalasoft.
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

import os
import cv2
from decouple import config

path_img = config('PATH_IMAGE')


# Load the image file
class LoadFiles:

    # Load the images of some person in order to train the model
    @staticmethod
    def load_img_train():
        images_train = []
        images_dict = {}
        for dirpath, dirnames, filenames in os.walk(path_img):
            path_components = dirpath.split(os.sep)
            name_path = path_components[-1]
            for f in filenames:
                images_train.append(cv2.imread('{}\{}'.format(dirpath, f)))
            if not images_train:
                pass
            else:
                images_dict[name_path] = images_train
                images_train = []
        return images_dict

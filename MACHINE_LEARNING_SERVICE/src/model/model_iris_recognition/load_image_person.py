#
# @load_image_person.py Copyright (c) 2022 Jalasoft.
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

import cv2


# Load the image file
class LoadFiles:
    def __init__(self, file: any):
        self.file: any = file

    # Load the iris of the person who is required to find
    def load_img_compare(self) -> None:
        image: None = cv2.imread(self.file)
        return image
    

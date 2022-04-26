#
# @uploader.py Copyright (c) 2022 Jalasoft.
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

from flask import request
import os


class Uploader:
    def __init__(self, request, save_location):
        self.request = request
        self.save_location = save_location

    def upload(self):
        if request.method == 'POST':
            fl = request.files['file']  # This is for the file, the rest is for converter imagen
            fl.save(os.path.join(self.save_location, fl.filename))
        return f"http://127.0.0.1:5000/download/{fl.filename}"  # return the image URL for download

    # this is for pass the params in the format that Said was using
    def _build_string_s(frame, color, format, width, height, quality):
        return f"{frame},{color},{format},{width},{height},{quality}"

    # this is for pass the params in the format that
    def _build_string_r(frame, color, format, width, height, quality):
        return (f"frame={frame}, color={color}, format={format}, width={width}, height={height},"
                f" quality={quality}")

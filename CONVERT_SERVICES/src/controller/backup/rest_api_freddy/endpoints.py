#
# @endpoints.py Copyright (c) 2022 Jalasoft.
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

from flask import Flask
from flask import request
from flask import send_file
import os

UPLOAD_FOLDER = 'savedfiles/'  # here is the file where the images will be downloaded

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/uploader', methods=['GET', 'POST'])  # We need pass this function to a class to use POO
def upload_file():  # you can have an idea how to make it in the Dayler part of the code for API
    if request.method == 'POST':
        fl = request.files['file']  # This is for the image file, the rest is for converter imagen
        fr = request.form.get('frame')
        cl = request.form.get('color')
        frm = request.form.get('format')
        wid = request.form.get('width')
        hei = request.form.get('height')
        qua = request.form.get('quality')  # These were the params that converter imagen needed
        fl.save(os.path.join(app.config['UPLOAD_FOLDER'], fl.filename))
    return f"http://127.0.0.1:5000/savedfiles/{fl.filename}"  # we return the image in download URL


def _build_string_s(frame, color, format, width, height, quality):  # this is for pass the params in
    return f"{frame},{color},{format},{width},{height},{quality}"   # the format that Said was using


def _build_string_r(frame, color, format, width, height, quality):  # this is for pass the params in
    return (f"frame={frame}, color={color}, format={format}, width={width},"  # the format that
            f" height={height}, quality={quality}")                           # Rodrigo was using


@app.route('/downloader/<string:file_name>')
def get_file(file_name):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], file_name), as_attachment=True)

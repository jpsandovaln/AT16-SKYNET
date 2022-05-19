#
# @convert_services_controller.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Condidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import connexion
import six

from swagger_server.models.success_convert_post import SuccessConvertPost  # noqa: E501
from swagger_server import util


def add_file(convert, file, frame, language_in, language_out, language, format, bitrate=None, sample_rate=None, audio_chanel=None, color=None, height=None, width=None, rotate=None, vertical_flip=None, horizontal_flip=None):  # noqa: E501
    """Add a new file deppending of service

     # noqa: E501

    :param convert: 
    :type convert: str
    :param file: Upload a new file
    :type file: werkzeug.datastructures.FileStorage
    :param frame: &#x60;Video&#x60;
    :type frame: float
    :param language_in: &#x60;Translator&#x60; and &#x60;WavTxt&#x60;
    :type language_in: str
    :param language_out: &#x60;Translator&#x60;
    :type language_out: str
    :param language: &#x60;OCR&#x60;
    :type language: str
    :param format:  &#x60;Audio Output_formats&#x60; [mp3, mp2, m4a and wav], &#x60;Video output_formats&#x60;{jpg,png}, &#x60;Image output_formats&#x60;[jpg, tiff, gif, webp, png and bmp], &#x60;translator output_formats&#x60;[txt],  &#x60;Wav_to_txt output_formats&#x60;{txt} &#x60;OCR output_formats&#x60;{txt, pdf and docx}, &#x60;Metadata output_formats&#x60;[txt, json and xmp]
    :type format: str
    :param bitrate: &#x60;Audio&#x60;
    :type bitrate: float
    :param sample_rate: &#x60;Audio&#x60;
    :type sample_rate: float
    :param audio_chanel: &#x60;Audio&#x60;
    :type audio_chanel: float
    :param color: &#x60;Image&#x60;[sRGB] and &#x60;Video&#x60;[RGB,gray]
    :type color: str
    :param height: &#x60;Image&#x60; and &#x60;Video&#x60;
    :type height: float
    :param width: &#x60;Image&#x60; and &#x60;Video&#x60;
    :type width: float
    :param rotate: &#x60;Image&#x60;
    :type rotate: 
    :param vertical_flip: &#x60;Image&#x60;
    :type vertical_flip: 
    :param horizontal_flip: &#x60;Image&#x60;
    :type horizontal_flip: 

    :rtype: SuccessConvertPost
    """
    return 'do some magic!'

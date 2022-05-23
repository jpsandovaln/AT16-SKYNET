#
# @parameters.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
#1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
#All rights reserved.
#
#This software is the confidential and proprietary information of
#Jalasoft, ("Condidential Information"). You shall # not
#disclose such Confidential Information and shall use it only in
#accordance with the terms of the license agreement you entered into
#with Jalasoft .
#

#By Rodrigo This class inherits the inputs of the converter.

from src.common.exceptions.parameter_exception import ParameterException
import os


class Parameters:
    def __init__(self, file: str, request: str):
        self.file: str = file
        self.request: str = request

    def validate(self):
        if os.path.split(self.file)[1] == "":
            raise ParameterException("Not file, put a file", "401","AT16-ERR-300")
        else:
            pass

    # Setting exceptions to the parameter exception module
    def validate_file(self):
        if self.file is None or str(self.file).strip() == "":
            raise ParameterException("Invalid file, the value is empty", "401",
                                     "AT16-ERR-300")
        else:
            pass
        is_file: any = os.path.isfile(self.file)

        if not is_file:
            raise ParameterException("It is not file", "402", "AT16-ERR-305")
        else:
            pass

    def validate_get_convert(self):
        converters: list = ['Image', 'Video', 'Metadata', 'Audio', 'OCR', 'Translator', 'WavTxt']
        if self.request.values.get('convert') == "":
            raise ParameterException("The convert filed is empty", "402", "AT16-ERR-305")
        elif self.request.values.get('convert') not in converters:
            raise ParameterException("Not a recognizer converter", "402", "AT16-ERR-305")
        else:
            pass

    def validate_format(self):
        ocr_converters: list = ['txt', 'docx', 'pdf']
        audio_converters: list = ['mp3', 'mp2', 'm4a', 'wav']
        video_converters: list = ['jpg', 'png']
        metadata_converters: list = ['txt', 'json', 'xmp']
        image_converters: list = ['jpg', 'tiff', 'gif', 'png', 'bmp', 'webp']
        translator_converters: list = ['txt']
        wav_converters: list = ['txt']
        if self.request.values.get('convert') == 'OCR' and self.request.values.get(
                'format') not in ocr_converters:
            raise ParameterException("format is Not a recognized format", "402", "AT16-ERR-305")
        elif self.request.values.get('convert') == 'Audio' and self.request.values.get(
                'format') not in audio_converters:
            raise ParameterException("format is Not a recognized format", "402", "AT16-ERR-305")
        elif self.request.values.get('convert') == 'Video' and self.request.values.get(
                'format') not in video_converters:
            raise ParameterException("format is Not a recognized format", "402", "AT16-ERR-305")
        elif self.request.values.get('convert') == 'Image' and self.request.values.get(
                'format') not in image_converters:
            raise ParameterException("format is Not a recognized format", "402", "AT16-ERR-305")
        elif self.request.values.get('convert') == 'Metadata' and self.request.values.get(
                'format') not in metadata_converters:
            raise ParameterException("format is Not a recognized format", "402", "AT16-ERR-305")
        elif self.request.values.get('convert') == 'Translator' and self.request.values.get(
                'format') not in translator_converters:
            raise ParameterException("format is Not a recognized format", "402", "AT16-ERR-305")
        elif self.request.values.get('convert') == 'WavTxt' and self.request.values.get(
                'format') not in wav_converters:
            raise ParameterException("format is Not a recognized format", "402", "AT16-ERR-305")
        else:
            pass

    def validate_in_format(self):
        ocr_converters: list = ['jpg', 'png']
        audio_converters: list = ['mp3', 'mp2', 'm4a', 'wav']
        video_converters: list = ['mp4', '3gp', 'mkv']
        image_converters: list = ['jpg', 'tiff', 'gif', 'png', 'bmp', 'webp']
        translator_converters: list = ['txt']
        wav_converters: list = ['wav']
        names: any = self.file.split('.')
        if self.request.values.get('convert') == 'OCR' and names[1].lower() not in ocr_converters:
            raise ParameterException("format file is Not a recognized format", "402",
                                     "AT16-ERR-307")
        elif self.request.values.get('convert') == 'Audio' and names[1].lower() not in \
                audio_converters:
            raise ParameterException("format file is Not a recognized format", "402",
                                     "AT16-ERR-306")
        elif self.request.values.get('convert') == 'Video' and names[1].lower() not in \
                video_converters:
            raise ParameterException("format file is Not a recognized format", "402",
                                     "AT16-ERR-306")
        elif self.request.values.get('convert') == 'Image' and names[1].lower() not in \
                image_converters:
            raise ParameterException("format file is Not a recognized format", "402",
                                     "AT16-ERR-306")
        elif self.request.values.get('convert') == 'Translator' and names[1].lower() not in \
                translator_converters:
            raise ParameterException("format file is Not a recognized format", "402",
                                     "AT16-ERR-306")
        elif self.request.values.get('convert') == 'WavTxt' and names[1].lower() not in \
                wav_converters:
            raise ParameterException("format file is Not a recognized format", "402",
                                     "AT16-ERR-306")
        else:
            pass

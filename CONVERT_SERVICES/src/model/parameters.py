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
    def __init__(self, file, request):
        self.file = file
        self.request = request

    def validate(self):
        if os.path.split(self.file)[1] == "":
            raise ParameterException("Not file, put a file", "401",
                                     "AT16-ERR-300")

    # Setting exceptions to the parameter exception module
    def validate_file(self):
        if self.file is None or str(self.file).strip() == "":
            raise ParameterException("Invalid file, the value is empty", "401",
                                     "AT16-ERR-300")
        is_file = os.path.isfile(self.file)

        if not is_file:
            raise ParameterException("It is not file", "402", "AT16-ERR-305")

    def validate_get_convert(self):
        converters = ['Image', 'Video', 'Metadata', 'Audio', 'OCR']
        if self.request.values.get('convert') == "":
            raise ParameterException("The convert filed is empty", "402", "AT16-ERR-305")
        if self.request.values.get('convert') not in converters:
            raise ParameterException("Not a recognizer converter", "402", "AT16-ERR-305")

    def validate_format(self):
        converters = ['txt', 'docx', 'pdf']
        if self.request.values.get('convert') == 'OCR' and self.request.values.get(
                'format') not in converters:
            raise ParameterException("format is Not a recognized format", "402", "AT16-ERR-305")

#
# parameters.py Copyright (c) 2022 Jalasoft.
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

from src.common.exceptions.parameter_exception import ParameterException
import os


# Parameters needed in order to find the owner of the iris.
class Parameters:
    def __init__(self, file, percentage):
        self.file = file
        self.percentage = percentage

    # Setting exceptions to the parameter exception module
    def validate(self):
        if os.path.split(self.file)[1] == "":
            raise ParameterException("Not file, put a file", "401",
                                     "AT16-ERR-300", "Iris recognition model")
        if self.file.endswith('.jpg') or self.file.endswith('.png') or self.file.endswith('.bmp'):
            pass
        else:
            raise ParameterException("Invalid format, "
                                     "the format needs to be jpg, png or bmp",
                                     "401", "AT16-ERR-300",
                                     "Iris recognition model")
        if self.percentage == "":
            raise ParameterException("Empty percentage", "401",
                                     "AT16-ERR-300",
                                     "Iris recognition model")
        if self.percentage.isalpha() or float(self.percentage) > 1 or float(self.percentage) \
                <= 0:
            raise ParameterException("Invalid percentage, "
                                     "the value needs to be major than 0 and "
                                     "less than 1", "401",
                                     "AT16-ERR-300",
                                     "Iris recognition model")

    # Setting exceptions to the parameter exception module
    def validate_file(self):
        if self.file is None or str(self.file).strip() == "":
            raise ParameterException("Invalid file, the value is empty", "401",
                                     "AT16-ERR-300", "Iris recognition model")
        is_file = os.path.isfile(self.file)

        if not is_file:
            raise ParameterException("It is not file", "402", "AT16-ERR-305",
                                     "Iris recognition model")


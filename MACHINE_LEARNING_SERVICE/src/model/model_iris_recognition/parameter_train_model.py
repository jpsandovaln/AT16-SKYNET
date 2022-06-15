#
# parameters_train_model.py Copyright (c) 2022 Jalasoft.
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


# Parameter needed in order to train the model
class ParametersTrainModel:
    def __init__(self, zip):
        self.zip = zip

    # Adding exceptions
    def validate(self):
        if os.path.split(self.zip)[1] == "":
            raise ParameterException("Not file, put a file", "401",
                                     "AT16-ERR-300", "Iris recognition model")
        if self.zip.endswith('.zip'):
            pass
        else:
            raise ParameterException("Invalid format, "
                                     "the format needs .zip",
                                     "401", "AT16-ERR-300",
                                     "Iris recognition model")

    # Adding exceptions
    def validate_file(self):
        if self.zip is None or str(self.zip).strip() == "":
            raise ParameterException("Invalid file, the value is empty", "401",
                                     "AT16-ERR-300", "Iris recognition model")
        is_file = os.path.isfile(self.zip)

        if not is_file:
            raise ParameterException("It is not file", "402", "AT16-ERR-305",
                                     "Iris recognition model")
            

#
# @controller_iris_train_model.py Copyright (c) 2022 Jalasoft.
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

from src.model.model_iris_recognition.train_model import TrainModel
from src.controller.utils.zipfile.zip import UnzipFile
import os
import json
from flask import Response
from http import HTTPStatus
from src.common.exceptions.machine_learning_exception import MachineLearningException
from src.controller.results.success_result import SuccessResult
from src.controller.results.error_result import ErrorResult
from src.model.model_iris_recognition.parameter_train_model import ParametersTrainModel
from flask import request


# This is for to upload a file.
class ControllerIrisTrain:
    def __init__(self, request, save_location):
        self.request = request
        self.save_location = save_location

    # This is for to request a file and a percentage
    def upload(self):
        if self.request.method == 'POST':
            try:
                zip_request = self.request.files['zip']
                path_saved_zip = os.path.join(self.save_location, zip_request.filename)
                parameters = ParametersTrainModel(path_saved_zip)
                parameters.validate()
                zip_request.save(path_saved_zip)
                parameters.validate_file()
                path_zip = UnzipFile(path_saved_zip)
                path_zip.decom_zip()

                result = TrainModel.train_model()
                result_model = SuccessResult(HTTPStatus.OK, str(result))
                return Response(
                    json.dumps(result_model.__dict__),
                    status=HTTPStatus.OK,
                    mimetype='application/json'
                )
            except MachineLearningException as error:
                result_error = ErrorResult(error.status, error.message,
                                           error.code)
                return Response(
                    json.dumps(result_error.__dict__),
                    status=error.status,
                    mimetype='application/json'
                )
            except Exception as error:
                result_error = ErrorResult(HTTPStatus.NOT_FOUND, error,
                                           'AT16-000451')
                return Response(
                    json.dumps(result_error.__dict__),
                    status=HTTPStatus.NOT_FOUND,
                    mimetype='application/json'
                )
            

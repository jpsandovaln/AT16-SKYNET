#
# @controller_iris_recognizer.py Copyright (c) 2022 Jalasoft.
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
from src.model.model_iris_recognition.model_iris import IrisModel
import os
import json
from flask import Response
from http import HTTPStatus
from src.common.exceptions.machine_learning_exception import MachineLearningException
from src.controller.results.success_result import SuccessResult
from src.controller.results.error_result import ErrorResult
from src.model.model_iris_recognition.parameters import Parameters


# This is for to upload a file.
class ControllerIris:
    def __init__(self, request: any, save_location: any):
        self.request: any = request
        self.save_location: any = save_location
        self.percentage_request: any = request.form.get('percentage')

    # This is for to request a file and a percentage
    def upload(self) -> dict:
        try:
            file_request: any = self.request.files['file']
            path_saved: bytes | str = os.path.join(self.save_location, file_request.filename)
            parameters: Parameters = Parameters(path_saved, self.percentage_request)
            parameters.validate()
            file_request.save(path_saved)  # To save the file
            parameters.validate_file()
            result: IrisModel = IrisModel(path_saved, self.percentage_request)
            result_model_iris: list[dict[str, float]] = result.matching_data()
            result_model: SuccessResult = SuccessResult(HTTPStatus.OK, str(result_model_iris))
            return Response(
                json.dumps(result_model.__dict__),
                status=HTTPStatus.OK,
                mimetype='application/json'
            )
        except MachineLearningException as error:
            result_error: ErrorResult = ErrorResult(error.status, error.message,
                                       error.code)
            return Response(
                json.dumps(result_error.__dict__),
                status=error.status,
                mimetype='application/json'
            )
        except Exception as error:
            result_error: ErrorResult = ErrorResult(HTTPStatus.NOT_FOUND, error,
                                       'AT16-000451')
            return Response(
                json.dumps(result_error.__dict__),
                status=HTTPStatus.NOT_FOUND,
                mimetype='application/json'
            )

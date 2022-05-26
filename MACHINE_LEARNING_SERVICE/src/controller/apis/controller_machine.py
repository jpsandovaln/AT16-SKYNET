#
# @controller_machine.py Copyright (c) 2022 Jalasoft.
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
from src.model.Result.model_result import ModelResult
from src.controller.utils.zipfile.decompress import Decompress
import os


# This is for to upload a file.
class ControllerMachineLearning:
    def __init__(self, request: any, save_location: any):
        self.request: any = request
        self.save_location: any = save_location

    # The function gets the zipped file, name and model. Returns a list of
    # images that contain the word.
    def upload(self) -> str:
        if self.request.method == 'POST':
            file_request: any = self.request.files['file']
            self.name_request: str | None = request.form.get('name')
            self.model_request: str | None = request.form.get('model')
            self.percentage_request: str | None = request.form.get('percentage')
            path_saved: bytes | str = os.path.join(self.save_location, file_request.filename)
            file_request.save(path_saved)
            path_zip: Decompress = Decompress(path_saved)
            path_zip_result: str = path_zip.path_decompress()
            result: ModelResult = ModelResult(path_zip_result, self.name_request,
                                 self.model_request, self.percentage_request)
            result_model: str = result.models_results()
            return result_model

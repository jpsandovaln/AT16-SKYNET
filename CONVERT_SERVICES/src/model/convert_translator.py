#
# @convert_translator.py Copyright (c) 2022 Jalasoft
# 2643 Av Melchor Perez de Olguin , Colquiri Sud, Cochabamba, Bolivia.
# add direccion de jala la paz>
# All rights reserved
#
# This software is the confidential and proprietary information of
# Jalasoft , Confidential Information "). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft


from deep_translator import GoogleTranslator
from http import HTTPStatus
from src.controller.results.error_result import ErrorResult
from src.common.exceptions.convert_exception import ConvertException
from src.common.exceptions.parameter_exception import ParameterException
from flask import Response
import json
from src.model.convertor import Convertor


class ConvertTranslator(Convertor):
    # Define the input of class
    def __init__(self, input_data: str, input_file: str):
        super().__init__(input_data, input_file)
        self.path: str = input_file  # input folder
        self.file: str = input_data.files['file'].filename
        self.instructions: str = self.get_instructions()
        self.language_in: str = self.instructions.values.get('language_in')
        self.language_out: str = self.instructions.values.get('language_out')

    # Define function for extract metadata
    def exec(self):
        try:
            language_in: str = self.language_in.split('-')
            language_out: str = self.language_out.split('-')
            translator: any = GoogleTranslator(source=language_in[0], target=language_out[0])
            file: any = open(self.input_file, mode='r')
            texto: str = file.read()
            result: any = translator.translate(texto)
            with open(self.output_file + '/' + self.name_output, mode='w') as file:
                file.write(result)
        except ConvertException as error:
            result_error: ErrorResult = ErrorResult(error.status, error.message, error.code)
            return Response(
                json.dumps(result_error.__dict__),
                status=error.status,
                mimetype='application/json'
            )
        except Exception as error:
            result_error: ErrorResult = ErrorResult(HTTPStatus.BAD_REQUEST, error, "AT16-ERROR-404")
            return Response(
                json.dumps(result_error.__dict__),
                status=HTTPStatus.NOT_FOUND,
                mimetype='application/json'
            )

#
# @convert_image.py Copyright (c)
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


from src.model.convertor import Convertor
from http import HTTPStatus
from src.controller.results.error_result import ErrorResult
from src.common.exceptions.convert_exception import ConvertException
from src.common.exceptions.parameter_exception import ParameterException
from flask import Response
import json
import os


class ConvertImage(Convertor):

    # constructor input folder, output folder
    def __init__(self, input_data: str, input_file: str):
        super().__init__(input_data, input_file)
        self.instructions: str = self.get_instructions()

    # Method to compare the data
    def init_dic(self):
        dic_param: dict = {'color': ' -colorspace {} ',
                           'rotate': ' -rotate {} ',
                           'vertical_flip': ' -flip ',
                           'horizontal_flip': ' -flop ',
                           'width': ' -resize {}',
                           'height': 'x{}! '}
        return dic_param

    # Method to create the ffmpeg command.
    def concatenate(self) -> str:
        dic: dict = self.init_dic()
        cod_cmd: str = "convert " + self.input_file + " "
        for key in dic:
            val: any = self.instructions.values.get(key)
            if len(val) > 0:
                if key == 'horizontal_flip' and val == 1:
                    dic[key]: dict = dic[key].format(val)
                    cod_cmd += dic[key]
                if key == 'vertical_flip' and val == 1:
                    dic[key]: dict = dic[key].format(val)
                    cod_cmd += dic[key]
                if key != 'horizontal_flip' and key != 'vertical_flip':
                    dic[key]: dict = dic[key].format(val)
                    cod_cmd += dic[key]
                    print(val+' - '+key)
            else:
                pass

        cod_cmd += self.output_file + '/' + self.name_output
        return cod_cmd

    # Method to converter the visual content.
    def exec(self):
        try:
            cod_cmd: str = self.concatenate()
            os.system(cod_cmd)
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


#
# @main.py Copyright (c) 2022 Jalasoft.
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

from flask import Flask
from flask_restful import Api
from flask import request
import json
from http import HTTPStatus
from src.controller.apis.search_report_start_finish_time_person_gender import SearchReportStartFinishTimePersonGender
from src.controller.apis.search_report_age_gender import SearchReportAgeGender
from src.controller.apis.search_report_date_person_country import SearchReportDatePersonCountry
from src.controller.apis.search_report_model_type import SearchReportModelType
from src.controller.apis.search_report_state_person_gender import SearchReportStatePersonGender
from src.controller.apis.search_report_subject_state import SearchReportSubjectState
from src.controller.apis.search_report_fil_time_location import SearchReportFilTimeLocation
from src.common.exceptions.reporting_exception import ReportingException
from src.controller.results.error_result import ErrorResult
from flask import Response

UPLOAD_FOLDER = 'saved_files/'  # here is the file where the images will be downloaded
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Api(app)


@app.route('/search_report_start_finish_time_person_gender', methods=['GET', 'POST'])
def search_report_start_finish_time_person_gender():
    try:
        report = SearchReportStartFinishTimePersonGender(request)
        return report.search_report_start_finish_time_person_gender()
    except ReportingException as error:
        result_error = ErrorResult("It is no posible consume", "400", "AT16-ERROR-404")
        return Response(
            json.dump(result_error.__dict__),
            status=error.status,
            mimetypes='aplication/json'
        )
    except Exception as error:
        result_error = ErrorResult(HTTPStatus.NOT_FOUND, error, "AT16-ERROR-404")
        return Response(
            json.dump(result_error.__dict__),
            status=HTTPStatus.NOT_FOUND,
            mimetypes='aplication/json'
        )

@app.route('/search_report_age_gender', methods=['GET', 'POST'])
def search_report_age_gender():
    try:
        report = SearchReportAgeGender(request)
        return report.search_report_age_gender()
    except ReportingException as error:
        result_error = ErrorResult("It is no posible consume", "400", "AT16-ERROR-404")
        return Response(
            json.dumps(result_error.__dict__),
            status=error.status,
            mimetypes='aplication/json'
        )
    except Exception as error:
        result_error = ErrorResult(HTTPStatus.NOT_FOUND, error, "AT16-ERROR-404")
        return Response(
            json.dumps(result_error.__dict__),
            status=HTTPStatus.NOT_FOUND,
            mimetypes='aplication/json'
        )


@app.route('/search_report_date_person_country', methods=['GET', 'POST'])
def search_report_date_person_country():
    try:
        report = SearchReportDatePersonCountry(request)
        return report.search_report_date_person_country()
    except ReportingException as error:
        result_error = ErrorResult("It is no posible consume", "400", "AT16-ERROR-404")
        return Response(
            json.dump(result_error.__dict__),
            status=error.status,
            mimetypes='aplication/json'
        )
    except Exception as error:
        result_error = ErrorResult(HTTPStatus.NOT_FOUND, error, "AT16-ERROR-404")
        return Response(
            json.dump(result_error.__dict__),
            status=HTTPStatus.NOT_FOUND,
            mimetypes='aplication/json'
        )


@app.route('/search_report_model_type', methods=['GET', 'POST'])
def search_report_model_type():
    try:
        report = SearchReportModelType(request)
        return report.search_report_model_type()
    except ReportingException as error:
        result_error = ErrorResult("It is no posible consume", "400", "AT16-ERROR-404")
        return Response(
            json.dump(result_error.__dict__),
            status=error.status,
            mimetypes='aplication/json'
        )
    except Exception as error:
        result_error = ErrorResult(HTTPStatus.NOT_FOUND, error, "AT16-ERROR-404")
        return Response(
            json.dump(result_error.__dict__),
            status=HTTPStatus.NOT_FOUND,
            mimetypes='aplication/json'
        )


@app.route('/search_report_state_person_gender', methods=['GET', 'POST'])
def search_report_state_person_gender():
    try:
        report = SearchReportStatePersonGender(request)
        return report.search_report_state_person_gender()
    except ReportingException as error:
        result_error = ErrorResult("It is no posible consume", "400", "AT16-ERROR-404")
        return Response(
            json.dump(result_error.__dict__),
            status=error.status,
            mimetypes='aplication/json'
        )
    except Exception as error:
        result_error = ErrorResult(HTTPStatus.NOT_FOUND, error, "AT16-ERROR-404")
        return Response(
            json.dump(result_error.__dict__),
            status=HTTPStatus.NOT_FOUND,
            mimetypes='aplication/json'
        )


@app.route('/search_report_subject_state', methods=['GET', 'POST'])
def search_report_subject_state():
    try:
        report = SearchReportSubjectState(request)
        return report.search_report_subject_state()
    except ReportingException as error:
        result_error = ErrorResult("It is no posible consume", "400", "AT16-ERROR-404")
        return Response(
            json.dump(result_error.__dict__),
            status=error.status,
            mimetypes='aplication/json'
        )
    except Exception as error:
        result_error = ErrorResult(HTTPStatus.NOT_FOUND, error, "AT16-ERROR-404")
        return Response(
            json.dump(result_error.__dict__),
            status=HTTPStatus.NOT_FOUND,
            mimetypes='aplication/json'
        )


@app.route('/search_report_fil_time_location', methods=['GET', 'POST'])
def search_report_fil_time_location():
    try:
        report = SearchReportFilTimeLocation(request)
        return report.search_report_fil_time_location()
    except ReportingException as error:
        result_error = ErrorResult("It is no posible consume", "400", "AT16-ERROR-404")
        return Response(
            json.dump(result_error.__dict__),
            status=error.status,
            mimetypes='aplication/json'
        )
    except Exception as error:
        result_error = ErrorResult(HTTPStatus.NOT_FOUND, error, "AT16-ERROR-404")
        return Response(
            json.dump(result_error.__dict__),
            status=HTTPStatus.NOT_FOUND,
            mimetypes='aplication/json'
        )

if __name__ == '__main__':
    app.run(debug=True)

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

from flask import Flask, jsonify
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
from src.reporting.connection import Connection
from src.reporting.criteria.criteria import Criteria
from src.reporting.parameters.parameter_report_age_gender import ParameterReportAgeGender
from src.reporting.parameters.parameter_report_model_type import ParameterReportModelType
from src.reporting.parameters.parameter_report_state_person_gender import \
    ParameterReportStatePersonGender

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


@app.route('/search_report_age_gender', methods=['POST'])
def search_report_age_gender():
    try:
        # Defines variables
        person_age = request.form.get('person_age')
        person_gender = request.form.get('person_gender')
        data_frame = Criteria.get_df()
        report = SearchReportAgeGender()

        # Gets the report
        parameters = ParameterReportAgeGender(person_age, person_gender, data_frame)
        result_report = report.search_report_age_gender(parameters)

        return Response(
            result_report,
            status=HTTPStatus.OK,
            mimetype='application/json'
        )

    except ReportingException as error:
        result_error = ErrorResult(error.status, error.message, error.code)
        return Response(
            json.dumps(result_error.__dict__),
            status=error.status,
            mimetype='application/json'
        )

    except Exception as error:
        result_error = ErrorResult(HTTPStatus.NOT_FOUND, error, "AT16-ERROR-404")
        return Response(
            json.dumps(result_error.__dict__),
            status=HTTPStatus.NOT_FOUND,
            mimetype='application/json'
        )


@app.route('/search_report_date_person_country', methods=['GET', 'POST'])
def search_report_date_person_country():
    try:
        report = SearchReportDatePersonCountry(request)
        return report.search_report_date_person_country()
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


@app.route('/search_report_model_type', methods=['POST'])
def search_report_model_type():
    try:
        # Defines variables
        resource_model = request.form.get('model')
        resource_type = request.form.get('type')
        data_frame = Criteria.get_df()
        report = SearchReportModelType()

        # Gets the report
        parameters = ParameterReportModelType(resource_model, resource_type, data_frame)
        result_report = report.search_report_model_type(parameters)

        return Response(
            result_report,
            status=HTTPStatus.OK,
            mimetype='application/json'
        )
    except ReportingException as error:
        result_error = ErrorResult(error.status, error.message, error.code)
        return Response(
            json.dumps(result_error.__dict__),
            status=error.status,
            mimetype='application/json'
        )
    except Exception as error:
        result_error = ErrorResult(HTTPStatus.NOT_FOUND, error, "AT16-ERROR-404")
        return Response(
            json.dumps(result_error.__dict__),
            status=HTTPStatus.NOT_FOUND,
            mimetype='application/json'
        )


@app.route('/search_report_state_person_gender', methods=['POST'])
def search_report_state_person_gender():
    try:
        # Defines variables
        state = request.form.get('state')
        person_gender = request.form.get('person_gender')
        data_frame = Criteria.get_df()
        report = SearchReportStatePersonGender()

        # Gets the report
        parameters = ParameterReportStatePersonGender(person_gender, state, data_frame)
        result_report = report.search_report_state_person_gender(parameters)

        return Response(
            result_report,
            status=HTTPStatus.OK,
            mimetype='application/json'
        )
    except ReportingException as error:
        result_error = ErrorResult(error.status, error.message, error.code)
        return Response(
            json.dumps(result_error.__dict__),
            status=error.status,
            mimetype='application/json'
        )
    except Exception as error:
        result_error = ErrorResult(HTTPStatus.NOT_FOUND, error, "AT16-ERROR-404")
        return Response(
            json.dumps(result_error.__dict__),
            status=HTTPStatus.NOT_FOUND,
            mimetype='application/json'
        )


@app.route('/search_report_subject_state', methods=['GET', 'POST'])
def search_report_subject_state():
    try:
        report = SearchReportSubjectState(request)
        return report.search_report_subject_state()
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


@app.route('/search_report_fil_time_location', methods=['GET', 'POST'])
def search_report_fil_time_location():
    try:
        report = SearchReportFilTimeLocation(request)
        return report.search_report_fil_time_location()
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

@app.route('/mongo_to_postgres', methods=['GET'])
def transfer_from_mongo_to_postgres():
    Connection.close_connection()
    return jsonify({
        "message": "Transfer from Mongo to Postgres, Success"
    })

@app.route('/verify', methods=['GET'])
def verify():
    return "Success!!"

if __name__ == '__main__':
    Connection.close_connection()
    app.run(host="0.0.0.0", debug=True, port=5001)

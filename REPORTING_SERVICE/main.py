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
from flask_cors import CORS
import json
from http import HTTPStatus

from src.controller.apis.search_report_start_finish_time_person_gender import SearchReportStartFinishTimePersonGender
from src.controller.apis.search_report_age_gender import SearchReportAgeGender
from src.controller.apis.search_report_date_person_country import SearchReportDatePersonCountry
from src.controller.apis.search_report_model_type import SearchReportModelType
from src.controller.apis.search_report_state_person_gender import SearchReportStatePersonGender
from src.controller.apis.search_report_fil_time_location import SearchReportFilTimeLocation
from src.common.exceptions.reporting_exception import ReportingException
from src.controller.results.error_result import ErrorResult
from flask import Response
from src.reporting.connection import Connection
from src.reporting.criteria.cache import Cache
from src.reporting.criteria.criteria import Criteria
from src.reporting.parameters.parameter_report_age_gender import ParameterReportAgeGender
from src.reporting.parameters.parameter_report_fill_time_location import \
    ParameterReportFillTimeLocation
from src.reporting.parameters.parameter_report_model_type import ParameterReportModelType
from src.reporting.parameters.parameter_report_state_person_gender import \
    ParameterReportStatePersonGender
from src.reporting.parameters.parameter_report_time_person_gender import \
    ParameterReportTimePersonGender
from src.reporting.parameters.parameter_report_date_person_country import \
    ParameterReportDatePersonCountry


app = Flask(__name__)
api = Api(app)
cors = CORS(app)


@app.route('/search_report_start_finish_time_person_gender', methods=['POST'])
def search_report_start_finish_time_person_gender():
    try:
        # Defines variables
        open_time: str = request.form.get('open_time')
        close_time: str = request.form.get('close_time')
        data_frame = Cache.load_cache()
        report = SearchReportStartFinishTimePersonGender()

        # Gets the report
        parameters = ParameterReportTimePersonGender(open_time, close_time, data_frame)
        result_report = report.search_report_start_finish_time_person_gender(parameters)

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
            mimetype='aplication/json'
        )


@app.route('/search_report_age_gender', methods=['POST'])
def search_report_age_gender():
    try:
        # Defines variables
        person_age: int = request.form.get('person_age')
        person_gender: str = request.form.get('person_gender')
        data_frame = Cache.load_cache()
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


@app.route('/search_report_date_person_country', methods=['POST'])
def search_report_date_person_country():
    try:
        # Defines variables
        start_date: str = request.form.get('start_date')
        end_date: str = request.form.get('end_date')
        data_frame = Cache.load_cache()
        report = SearchReportDatePersonCountry()

        # Gets the report
        parameters = ParameterReportDatePersonCountry(start_date, end_date,
                                                      data_frame)
        result_report = report.search_report_date_person_country(parameters)
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
            mimetype='aplication/json'
        )

    except Exception as error:
        result_error = ErrorResult(HTTPStatus.NOT_FOUND, error, "AT16-ERROR-404")
        return Response(
            json.dumps(result_error.__dict__),
            status=HTTPStatus.NOT_FOUND,
            mimetype='aplication/json'
        )


@app.route('/search_report_model_type', methods=['POST'])
def search_report_model_type():
    try:
        # Defines variables
        resource_model: str = request.form.get('model')
        resource_type: str = request.form.get('type')
        data_frame = Cache.load_cache()
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
        state: str = request.form.get('state')
        person_gender: str = request.form.get('person_gender')
        data_frame = Cache.load_cache()
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


@app.route('/search_report_fill_time_location', methods=['POST'])
def search_report_fill_time_location():
    try:
        # Defines variables
        start_date: str = request.form.get('start_date')
        end_date: str = request.form.get('end_date')
        data_frame = Cache.load_cache()
        report = SearchReportFilTimeLocation()

        # Gets the report
        parameters = ParameterReportFillTimeLocation(start_date, end_date,
                                                     data_frame)
        result_report = report.search_report_fil_time_location(parameters)
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
        result_error = ErrorResult(HTTPStatus.NOT_FOUND, error,
                                   "AT16-ERROR-404")
        return Response(
            json.dumps(result_error.__dict__),
            status=HTTPStatus.NOT_FOUND,
            mimetype='application/json'
        )


@app.route('/mongo_to_postgres', methods=['GET'])
def transfer_from_mongo_to_postgres():
    try:
        Connection.close_connection()
        Criteria.get_df()
        result_report = "Transfer from Mongo to Postgres, Success"
        return Response(
            json.dumps(result_report),
            status=HTTPStatus.OK,
            mimetype='application/json'
        )
    except Exception as error:
        result_error = ErrorResult(HTTPStatus.NOT_FOUND, error,
                                   "AT16-ERROR-404")
        return Response(
            json.dumps(result_error.__dict__),
            status=HTTPStatus.NOT_FOUND,
            mimetype='application/json'
        )


if __name__ == '__main__':
    Connection.close_connection()
    Criteria.get_df()
    app.run(host="0.0.0.0", debug=True, port=5001)

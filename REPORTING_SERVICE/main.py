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

from src.controller.apis.search_report_start_finish_time_person_gender import SearchReportStartFinishTimePersonGender
from src.controller.apis.downloader import Downloader
from src.controller.apis.search_report_age_gender import SearchReportAgeGender
from src.controller.apis.search_report_date_person_country import SearchReportDatePersonCountry
from src.controller.apis.search_report_model_type import SearchReportModelType
from src.controller.apis.search_report_state_person_gender import SearchReportStatePersonGender
from src.controller.apis.search_report_subject_state import SearchReportSubjectState
from src.controller.apis.search_report_fil_time_location import SearchReportFilTimeLocation

UPLOAD_FOLDER = 'saved_files/'  # here is the file where the images will be downloaded

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Api(app)


@app.route('/search_report_start_finish_time_person_gender', methods=['GET', 'POST'])
def save_file():
    report = SearchReportStartFinishTimePersonGender(request)
    return report.search_report_start_finish_time_person_gender()


@app.route('/search_report_age_gender', methods=['GET', 'POST'])
def save_file_1():
    report = SearchReportAgeGender(request)
    return report.search_report_age_gender()


@app.route('/search_report_date_person_country', methods=['GET', 'POST'])
def save_file_2():
    report = SearchReportDatePersonCountry(request)
    return report.search_report_date_person_country()


@app.route('/search_report_model_type', methods=['GET', 'POST'])
def save_file_3():
    report = SearchReportModelType(request)
    return report.search_report_model_type()


@app.route('/search_report_state_person_gender', methods=['GET', 'POST'])
def save_file_4():
    report = SearchReportStatePersonGender(request)
    return report.search_report_state_person_gender()


@app.route('/search_report_subject_state', methods=['GET', 'POST'])
def save_file_5():
    report = SearchReportSubjectState(request)
    return report.search_report_subject_state()


@app.route('/search_report_fil_time_location', methods=['GET', 'POST'])
def save_file_6():
    report = SearchReportFilTimeLocation(request)
    return report.search_report_fil_time_location()


@app.route('/download/<string:file_name>')
def download_file(file_name):
    file = Downloader(request, app.config['UPLOAD_FOLDER'], file_name)
    return file.donwload()


if __name__ == '__main__':
    app.run(debug=True)

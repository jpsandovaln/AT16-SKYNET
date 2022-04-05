#
# @search_report.py Copyright (c) 2022 Jalasoft.
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
from src.reporting.criteria.filters_date_person_country import Filters_Date_Person_Country




class SearchReport2:
    def __init__(self, request):
        self.request = request


    def search_report_2(self):
        if request.method == 'POST':
                file_route = request.form.get('file_route')  # This is for the file, the rest is for converter imagen
                date = request.form.get('date')
                person_country = request.form.get('person_country')
                Criteria = Filters_Date_Person_Country(str(date), str(person_country), str(file_route))
        #print(Criteria.get_df()[Criteria.fil_time_location()])
        return str(Criteria.get_df()[Criteria.filters_date_person_country()])

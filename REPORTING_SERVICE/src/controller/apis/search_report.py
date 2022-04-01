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
from src.reporting.criteria.filters import Filters
from src.reporting.criteria.criteria import Criteria

class SearchReport:
    def __init__(self, request):
        self.request = request

    def search_report(self):
        if request.method == 'POST':
            file_route = request.form.get('file_route')  # This is for the file, the rest is for converter imagen
            star_time = request.form.get('star_time')
            end_time = request.form.get('end_time')
            location = request.form.get('location')
            #print('Route: '+ file_route + 'Hora inicio: '+ star_time + 'Hora fin: '+ end_time + 'Pais: '+ location)
            Criteria = Filters(6, 16, location, file_route)
        return Criteria.fil()  # return the image URL for download

    # this is for pass the params in the format that Said was using
    def _build_string_s(frame, color, format, width, height, quality):
        return f"{frame},{color},{format},{width},{height},{quality}"

    # this is for pass the params in the format that
    def _build_string_r(frame, color, format, width, height, quality):
        return (f"frame={frame}, color={color}, format={format}, width={width}, height={height},"
                f" quality={quality}")

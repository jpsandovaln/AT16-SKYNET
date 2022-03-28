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

from flask import send_file
from flask_restful import Resource


class FileDownloader(Resource):
    def get(self, file_id):
        name = f"{file_id}.jpg"
        filepath = f"files/{name}"

        file = send_file(
            path_or_file=filepath,
            mimetype="application/octet-stream",
            as_attachment=True,
            attachment_filename=name
        )
        return file

    def delete(self, file_id):
        pass

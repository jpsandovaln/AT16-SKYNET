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
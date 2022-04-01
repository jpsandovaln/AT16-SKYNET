import werkzeug
from flask_restful import Resource, reqparse


class FileUploader(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        parse.add_argument('name', type=str)
        args = parse.parse_args()
        image_file = args['file']
        name = args['name']
        filename = f"{name}.jpg"
        image_file.save(f"files/{filename}")
        return {"file_id": filename}

    def get(self):
        pass
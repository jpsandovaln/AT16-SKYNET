from flask import Flask
from flask_restful import Api

from rest_api.resources.downloader import FileDownloader
from rest_api.resources.uploader import FileUploader

app = Flask(__name__)
api = Api(app)


api.add_resource(FileUploader, '/files')
api.add_resource(FileDownloader, '/file/<string:file_id>')

if __name__ == '__main__':
    app.run(debug=True)
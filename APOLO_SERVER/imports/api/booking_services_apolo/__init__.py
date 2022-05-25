import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://ngimluxm:zK59sGLE3DXX41RwivZ3MoceL5zGMqSu@stampy.db.elephantsql.com:5432/ngimluxm"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)



@app.route('/')
def hello():
    url = 'http://127.0.0.1:6002/resource'
    response = requests.get(url)
    return (response.json())
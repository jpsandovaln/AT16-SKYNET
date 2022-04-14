#
# @__init__.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
# Create a simple Flask server
app = Flask(__name__)
CORS(app)
# Add the database url
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://jsxoccwf:zFlKN8ZbqT0OQgI9M1pmgQDEYfSqL0IE@manny.db.elephantsql.com/jsxoccwf"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'My First API !!'
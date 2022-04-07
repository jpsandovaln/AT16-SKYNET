#
# @main.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Condidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from src.model.resource import Resource
from src.model.person import Person
from src.model.booking import Booking
from flask import Flask, request, Response, jsonify


app = Flask(__name__)


# Create a Resource for Booking
@app.route('/resource', methods=['POST'])
def create_resource():
    resource = Resource()
    result = resource.resource_create(request.json)
    return jsonify(result)

# Get all Resources of the Database of Booking
@app.route('/resource', methods=['GET'])
def get_resource_all():
    resource = Resource()
    result = resource.resource_read_all()
    return jsonify(result)


# Get a Resource by Id of the Database of Booking
@app.route('/resource/id/<string:id_resource>', methods=['GET'])
def get_resource_by_id(id_resource):
    resource = Resource()
    result = resource.resource_read_specific_id(id_resource)
    return jsonify(result)


# Get a Resource by Name of the Database of Booking
@app.route('/resource/name/<string:resource_name>', methods=['GET'])
def get_resource_by_name(resource_name):
    resource = Resource()
    result = resource.resource_read_specific_name({"name":str(resource_name)})
    return jsonify(result)


# Update a Resource by Id of the Database of Booking
@app.route('/resource/<string:id_resource>', methods=['PUT'])
def update_resource(id_resource):
    resource = Resource()
    result = resource.resource_update(id_resource, request.json)
    return jsonify(result)


# Delete a Resource by Id of the Database of Booking
@app.route('/resource/<string:id_resource>', methods=['DELETE'])
def delete_resource(id_resource):
    resource = Resource()
    result = resource.resource_delete(id_resource)
    return jsonify(result)


# Create a Person into the Database of Booking
@app.route('/person', methods=['POST'])
def create_person():
    person = Person()
    result = person.person_create(request.json)
    return jsonify(result)


# Get all Persons of the Database of Booking
@app.route('/person', methods=['GET'])
def get_person_all():
    person = Person()
    result = person.person_read_all()
    return jsonify(result)


# Get a Person by Id of the Database of Booking
@app.route('/person/id/<string:id_person>', methods=['GET'])
def get_person_by_id(id_person):
    person = Person()
    result = person.person_read_specific_id(id_person)
    return jsonify(result)


# Get a Person by Name of the Database of Booking
@app.route('/person/name/<string:person_name>', methods=['GET'])
def get_person_by_name(person_name):
    person = Person()
    result = person.person_read_specific_name({"person_full_name": str(person_name)})
    return jsonify(result)


# Update a Person by Id of the Database of Booking
@app.route('/person/<string:id_person>', methods=['PUT'])
def update_person(id_person):
    person = Person()
    result = person.person_update(id_person, request.json)
    return jsonify(result)

# Delete a Person by Id of the Database of Booking
@app.route('/person/<string:id_person>', methods=['DELETE'])
def delete_person(id_person):
    person = Person()
    result = person.person_delete(id_person)
    return jsonify(result)


# Create a Booking
@app.route('/booking', methods=['POST'])
def create_booking():
    booking = Booking()
    result = booking.booking_create(request.json)
    return jsonify(result)


# Get all booking of the DataBase
@app.route('/booking', methods=['GET'])
def get_booking_all():
    booking = Booking()
    result = booking.booking_read_all()
    return jsonify(result)


@app.route('/booking/id/<string:id_booking>', methods=['GET'])
def get_booking_by_id(id_booking):
    booking = Booking()
    result = booking.booking_read_specific_id(id_booking)
    return jsonify(result)


# Update a Booking by Id
@app.route('/booking/id/<string:id_booking>', methods=['PUT'])
def update_booking(id_booking):
    booking = Booking()
    result = booking.booking_update(id_booking, request.json)
    return jsonify(result)


# Delete a booking of the DataBase
@app.route('/booking/<string:id_booking>', methods=['DELETE'])
def delete_booking(id_booking):
    booking = Booking()
    result = booking.booking_delete(id_booking)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

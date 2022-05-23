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


app: Flask = Flask(__name__)


# Create a Resource for Booking
@app.route('/resource', methods=['POST'])
def create_resource() -> dict:
    resource: Resource = Resource()
    result: str = resource.resource_create(request.json)
    return jsonify(result)


# Get all Resources of the Database of Booking
@app.route('/resource', methods=['GET'])
def get_resource_all() -> dict:
    resource: Resource = Resource()
    result: str = resource.resource_read_all()
    return jsonify(result)


# Get a Resource by Id of the Database of Booking
@app.route('/resource/id/<string:id_resource>', methods=['GET'])
def get_resource_by_id(id_resource) -> dict:
    resource: Resource = Resource()
    result: str = resource.resource_read_specific_id(id_resource)
    return jsonify(result)


# Get a Resource by Name of the Database of Booking
@app.route('/resource/name/<string:resource_name>', methods=['GET'])
def get_resource_by_name(resource_name) -> dict:
    resource: Resource = Resource()
    result: str = resource.resource_read_specific_name({"name":str(resource_name)})
    return jsonify(result)


# Update a Resource by Id of the Database of Booking
@app.route('/resource/<string:id_resource>', methods=['PUT'])
def update_resource(id_resource) -> dict:
    resource: Resource = Resource()
    result: str = resource.resource_update(id_resource, request.json)
    return jsonify(result)


# Delete a Resource by Id of the Database of Booking
@app.route('/resource/<string:id_resource>', methods=['DELETE'])
def delete_resource(id_resource) -> dict:
    resource: Resource = Resource()
    result: str = resource.resource_delete(id_resource)
    return jsonify(result)


# Create a Person into the Database of Booking
@app.route('/person', methods=['POST'])
def create_person() -> dict:
    person: Person = Person()
    result: str = person.person_create(request.json)
    return jsonify(result)


# Get all Persons of the Database of Booking
@app.route('/person', methods=['GET'])
def get_person_all() -> dict:
    person: Person = Person()
    result: str = person.person_read_all()
    return jsonify(result)


# Get a Person by Id of the Database of Booking
@app.route('/person/id/<string:id_person>', methods=['GET'])
def get_person_by_id(id_person) -> dict:
    person: Person = Person()
    result: str = person.person_read_specific_id(id_person)
    return jsonify(result)


# Get a Person by Name of the Database of Booking
@app.route('/person/name/<string:person_name>', methods=['GET'])
def get_person_by_name(person_name) -> dict:
    person: Person = Person()
    result: str = person.person_read_specific_name({"person_full_name": str(person_name)})
    return jsonify(result)


# Update a Person by Id of the Database of Booking
@app.route('/person/<string:id_person>', methods=['PUT'])
def update_person(id_person) -> dict:
    person: Person = Person()
    result: str = person.person_update(id_person, request.json)
    return jsonify(result)


# Delete a Person by Id of the Database of Booking
@app.route('/person/<string:id_person>', methods=['DELETE'])
def delete_person(id_person) -> dict:
    person: Person = Person()
    result: str = person.person_delete(id_person)
    return jsonify(result)


# Create a Booking
@app.route('/booking', methods=['POST'])
def create_booking() -> dict:
    booking: Booking = Booking()
    result: str = booking.booking_create(request.json)
    return jsonify(result)


# Get all booking of the DataBase
@app.route('/booking', methods=['GET'])
def get_booking_all() -> dict:
    booking: Booking  = Booking()
    result: str = booking.booking_read_all()
    return jsonify(result)


# Get a Booking by Id
@app.route('/booking/id/<string:id_booking>', methods=['GET'])
def get_booking_by_id(id_booking) -> dict:
    booking: Booking  = Booking()
    result: str = booking.booking_read_specific_id(id_booking)
    return jsonify(result)


# Update a Booking by Id
@app.route('/booking/<string:id_booking>', methods=['PUT'])
def update_booking(id_booking) -> dict:
    booking: Booking  = Booking()
    result: str = booking.booking_update(id_booking, request.json)
    return jsonify(result)


# Delete a booking of the DataBase
@app.route('/booking/<string:id_booking>', methods=['DELETE'])
def delete_booking(id_booking) -> dict:
    booking: Booking  = Booking()
    result: str = booking.booking_delete(id_booking)
    return jsonify(result)


# End Point just to verify
@app.route('/verify', methods=['GET'])
def verify():
    return jsonify({"message": "success!!"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)

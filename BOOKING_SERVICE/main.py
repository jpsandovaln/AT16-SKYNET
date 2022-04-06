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


# Endpoint resource
@app.route('/CreateResource', methods=['POST'])
def create_resource():
    resource = Resource()
    result = resource.resource_create(request.json)
    return jsonify(result)


@app.route('/GetResourceAll', methods=['GET'])
def get_resource_all():
    resource = Resource()
    result = resource.resource_read_all()
    return jsonify(result)


@app.route('/GetResourceById/<string:id_resource>', methods=['GET'])
def get_resource_by_id(id_resource):
    resource = Resource()
    result = resource.resource_read_specific_id(id_resource)
    return jsonify(result)


@app.route('/GetResourceByName', methods=['GET'])
def get_resource_by_name():
    resource = Resource()
    result = resource.resource_read_specific_name(request.json)
    return jsonify(result)


@app.route('/UpdateResource/<string:id_resource>', methods=['PUT'])
def update_resource(id_resource):
    resource = Resource()
    result = resource.resource_update(id_resource, request.json)
    return jsonify(result)


@app.route('/DeleteResource/<string:id_resource>', methods=['DELETE'])
def delete_resource(id_resource):
    resource = Resource()
    result = resource.resource_delete(id_resource)
    return jsonify(result)


# Endpoint person
@app.route('/CreatePerson', methods=['POST'])
def create_person():
    person = Person()
    result = person.person_create(request.json)
    return jsonify(result)


@app.route('/GetPersonAll', methods=['GET'])
def get_person_all():
    person = Person()
    result = person.person_read_all()
    return jsonify(result)


@app.route('/GetPersonById/<string:id_person>', methods=['GET'])
def get_person_by_id(id_person):
    person = Person()
    result = person.person_read_specific_id(id_person)
    return jsonify(result)


@app.route('/GetPersonByName', methods=['GET'])
def get_person_by_name():
    person = Person()
    result = person.person_read_specific_name(request.json)
    return jsonify(result)


@app.route('/UpdatePerson/<string:id_person>', methods=['PUT'])
def update_person(id_person):
    person = Person()
    result = person.person_update(id_person, request.json)
    return jsonify(result)


@app.route('/DeletePerson/<string:id_person>', methods=['DELETE'])
def delete_person(id_person):
    person = Person()
    result = person.person_delete(id_person)
    return jsonify(result)


# Endpoint booking
@app.route('/CreateBooking', methods=['POST'])
def create_booking():
    booking = Booking()
    result = booking.booking_create(request.json)
    return jsonify(result)


@app.route('/GetBookingAll', methods=['GET'])
def get_booking_all():
    booking = Booking()
    result = booking.booking_read_all()
    return jsonify(result)


@app.route('/GetBookingById/<string:id_booking>', methods=['GET'])
def get_booking_by_id(id_booking):
    booking = Booking()
    result = booking.booking_read_specific_id(id_booking)
    return jsonify(result)


@app.route('/GetBookingByName', methods=['GET'])
def get_booking_by_name():
    booking = Booking()
    result = booking.booking_read_specific_name(request.json)
    return jsonify(result)


@app.route('/UpdateBooking/<string:id_booking>', methods=['PUT'])
def update_booking(id_booking):
    booking = Booking()
    result = booking.booking_update(id_booking, request.json)
    return jsonify(result)


@app.route('/DeleteBooking/<string:id_booking>', methods=['DELETE'])
def delete_booking(id_booking):
    booking = Booking()
    result = booking.booking_delete(id_booking)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

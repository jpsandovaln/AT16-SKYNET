from flask.json import dumps

from src.model.resource import Resource
from src.model.person import Person
from flask import Flask, request, Response, jsonify
app = Flask(__name__)
from bson.objectid import ObjectId
from bson.json_util import dumps,RELAXED_JSON_OPTIONS


# Endpoint resource
@app.route('/CreateResource', methods=['POST'])
def create_resource():
    resource = Resource()
    resource_created = resource.resource_create({
        "name": request.json['name'],
        "type": request.json['type'],
        "model": request.json['model'],
        "state": request.json['state']
        })

    resource_found = resource.resource_read_specific_id(resource_created.inserted_id)
    resource_dict = {
        "name": resource_found['name'],
        "type": resource_found['type'],
        "model": resource_found['model'],
        "state": resource_found['state']}

    return jsonify(resource_dict)

@app.route('/UpdateResource/<string:id_resource>', methods=['PUT'])
def update_resource(id_resource):
    resource = Resource()
    variable = request.json
    result = resource.resource_update(id_resource, variable)
    return dumps(str(result))

@app.route('/GetResources', methods=['GET'])
def get_resources():
    resource = Resource()
    result = resource.resource_read_all()
    result_dict = []
    for result_by_element in result:
        resource_dict = {
            "id": str(ObjectId(result_by_element['_id'])),
            "name": result_by_element['name'],
            "type": result_by_element['type'],
            "model": result_by_element['model'],
            "state": result_by_element['state']
            }
        result_dict.append(resource_dict)
    return jsonify(result_dict)

# Endpoint person
@app.route('/CreatePerson', methods=['POST'])
def create_person():
    person = Person()
    result = person.person_create(request.json)
    result['_id'] = str(result['_id'])
    return jsonify(result)

@app.route('/UpdatePerson/<string:id_person>', methods=['PUT'])
def update_person(id_person):
    person = Person()
    data_update = request.json
    result = person.person_update(id_person, data_update)
    return dumps(str(result))

@app.route('/GetPerson/<string:id_person>', methods=['GET'])
def get_person(id_person):
    person = Person()
    result = person.person_read_all()
    result_dict = []
    for result_by_element in result:
        person_dict = {
            "id": str(ObjectId(result_by_element['_id'])),
            "person_full_name": result_by_element['person_full_name'],
            "person_age": result_by_element['person_age'],
            "person_country": result_by_element['person_country'],
            "person_city": result_by_element['person_city'],
            "person_gender": result_by_element['person_gender'],
            }
        result_dict.append(person_dict)
    return jsonify(result_dict)

@app.route('/DeletePerson/<string:id_person>', methods=['DELETE'])
def delete_person(id_person):
    person = Person()
    result = person.person_delete(id_person)
    return dumps(str(result))



# Endpoint booking


if __name__ == '__main__':
    app.run(debug=True)


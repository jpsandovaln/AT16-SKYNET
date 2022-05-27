from app import db
import json

class Post(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    resource_name = db.Column(db.String)
    resource_type = db.Column(db.String)
    resource_model = db.Column(db.String)
    resource_state = db.Column(db.String)

    def to_dict(self):
        return {
            "resource_name": self.resource_name,
            "resource_type": self.resource_type,
            "resource_model": self.resource_model,
            "resource_state": self.resource_state
        }


class Person(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    person_age = db.Column(db.String)
    person_city = db.Column(db.String)
    person_country = db.Column(db.String)
    person_full_name = db.Column(db.String)
    person_gender = db.Column(db.String)

    def to_dict(self):
        return {
            "person_age": self.person_age,
            "person_city": self.person_city,
            "person_country": self.person_country,
            "person_full_name": self.person_full_name,
            "person_gender": self.person_gender
        }

class Person_put:
    def __init__(self, person_age, person_city, person_country, person_full_name, person_gender):
        self.person_age = person_age
        self.person_city = person_city
        self.person_country = person_country
        self.person_full_name = person_full_name
        self.person_gender = person_gender

    def to_dict(self):
        parameters = [self.person_age, self.person_city, self.person_country, self.person_full_name, self.person_gender]
        string_to_convert = "{"

        if parameters[0] != "" and parameters [0] != None:
            string_to_convert += '"person_age": ' + '"' + parameters[0] + '"'+ ','
        if parameters[1] != "" and parameters [1] != None:
            string_to_convert += '"person_city": ' + '"' + parameters[1] + '"' + ','
        if parameters[2] != "" and parameters [2] != None:
            string_to_convert += '"person_country": ' + '"' + parameters[2] + '"' + ','
        if parameters[3] != "" and parameters [3] != None:
            string_to_convert += '"person_full_name": ' + '"' + parameters[3] + '"' + ','
        if parameters[4] != "" and parameters [4] != None:
            string_to_convert += '"person_gender": ' + '"' + parameters[4] + '"' + ','
        #string_to_convert += "}"
        string_cleared = string_to_convert[:-1]
        string_cleared += "}"


        json_object = json.loads(string_cleared)
        return json_object

class Booking_put:
    def __init__(self, description, subject, person_id, resource_id, date, end_time, start_time, state, type):
        self.description = description
        self.subject = subject
        self.person_id = person_id
        self.resource_id = resource_id
        self.date = date
        self.end_time = end_time
        self.start_time = start_time
        self.state = state
        self.type = type

    def to_dict(self):
        parameters = [self.description, self.subject, self.person_id, self.resource_id, self.date, self.end_time,
                      self.start_time, self.state, self.type]
        string_to_convert = "{"
        if (parameters[0] != "" and parameters[0] != None) or (parameters[1] != "" and parameters[1] != None):
            string_to_convert += '"details":{'
            if parameters[0] != "" and parameters[0] != None:
                string_to_convert += '"description": ' + '"' + parameters[0] + '"' + ','
            if parameters[1] != "" and parameters[1] != None:
                string_to_convert += '"subject": ' + '"' + parameters[1] + '"' + ','
            string_to_convert = string_to_convert[:-1]
            string_to_convert += "}, "
        if parameters[2] != "" and parameters[2] != None:
            string_to_convert += '"person":{'
            string_to_convert += '"id": ' + '"' + parameters[2] + '"'
            string_to_convert += "},"
        if parameters[3] != "" and parameters[3] != None:
            string_to_convert += ' "resource":{'
            string_to_convert += '"id": ' + '"' + parameters[3] + '"'
            string_to_convert += "},"
        if (parameters[4] != "" and parameters[4] != None) or (parameters[5] != "" and parameters[5] != None) or (
                parameters[6] != "" and parameters[6] != None):
            string_to_convert += ' "schedule":{'
            if parameters[4] != "" and parameters[4] != None:
                string_to_convert += '"date": ' + '"' + parameters[4] + '"' + ','
            if parameters[5] != "" and parameters[5] != None:
                string_to_convert += '"end_time": ' + '"' + parameters[5] + '"' + ','
            if parameters[6] != "" and parameters[6] != None:
                string_to_convert += '"start_time": ' + '"' + parameters[6] + '"' + ','
            string_to_convert = string_to_convert[:-1]
            string_to_convert += "},"
        if parameters[7] != "" and parameters[7] != None:
            string_to_convert += '"state": ' + '"' + parameters[7] + '"' + ','
        if parameters[8] != "" and parameters[8] != None:
            string_to_convert += '"type": ' + '"' + parameters[8] + '"' + ','
        string_cleared = string_to_convert[:-1]
        string_cleared = string_cleared[:-1]
        string_cleared += "}"

        json_object = json.loads(string_cleared)
        return json_object





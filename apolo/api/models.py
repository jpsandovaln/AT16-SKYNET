from app import db


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

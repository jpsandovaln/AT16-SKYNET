from datetime import date

from ariadne import convert_kwargs_to_snake_case

from api import db
from api.models import Post, Person
from decouple import config
address = config('address')
import requests


@convert_kwargs_to_snake_case
def create_post_resolver(obj, info, name, type, model, state):
    try:
        url = address + '/resource'
        post = Post(
            resource_name=name,
            resource_type=type,
            resource_model=model,
            resource_state=state
        )
        response = requests.post(url, json=post.to_dict())
        payload = {

            "success": True,
            "post": response.json()
        }
    except ValueError:  # date format errors

        payload = {

            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }

    return payload


@convert_kwargs_to_snake_case
def update_post_resolver(obj, info, id_source, name):
    try:
        url = address + '/resource/' + id_source
        dates = {'resource_name': name}

        response = requests.put(url, json=dates)
        payload = {
            "success": True,
            "post": response.json()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def delete_post_resolver(obj, info, id_source):
    try:
        url = address + '/resource/' + id_source
        response = requests.delete(url)

        payload = {"success": True,
                   "post": response.json()
                   }

    except AttributeError:
        print(db)
        payload = {
            "success": False,
            "errors": ["Not found"]
        }

    return payload

# methods for person
@convert_kwargs_to_snake_case
def create_post_resolver_person(obj, info, name, age, city, country, gender):
    try:
        url = address + '/person'

        post = Person(
            person_age=age,
            person_city = city,
            person_country = country,
            person_full_name = name,
            person_gender = gender
        )
        response = requests.post(url, json=post.to_dict())
        payload = {

            "success": True,
            "post": response.json()
        }
    except ValueError:  # date format errors

        payload = {

            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }

    return payload


@convert_kwargs_to_snake_case
def update_post_resolver_person(obj, info, id_person, city):
    try:
        url = address + '/person/' + id_person
        dates = {'person_city': city}
        response = requests.put(url, json=dates)
        payload = {
            "success": True,
            "post": response.json()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }

    return payload
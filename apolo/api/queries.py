import requests
from decouple import config

address = config('address')
from .models import Post
from ariadne import convert_kwargs_to_snake_case


def listPosts_resolver(obj, info):
    try:
        url = address + '/resource'
        response = requests.get(url)
        payload = {
            "success": True,
            "posts": response.json()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def getPost_resolver(obj, info, id):
    try:
        url = address + '/resource/id/' + id
        response = requests.get(url)
        payload = {
            "success": True,
            "post": response.json()
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Todo item matching id {id} not found"]
        }

    return payload

def listPosts_resolver_person(obj, info):
    try:
        url = address + '/person'
        response = requests.get(url)
        payload = {
            "success": True,
            "posts": response.json()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def getPost_resolver_person(obj, info, id):
    try:
        url = address + '/person/id/' + id
        response = requests.get(url)
        payload = {
            "success": True,
            "post": response.json()
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Todo item matching id {id} not found"]
        }

    return payload
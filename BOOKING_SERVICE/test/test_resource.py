import unittest
import requests
from src.model.resource import Resource
from bson.objectid import ObjectId


class ResourceTest(unittest.TestCase):
    URI = "http://127.0.0.1:6002/resource"
    BOOK_URI = "{}/name".format(URI)
    OBJECT_VALUE = {
        "resource_name": "Notebook2002",
        "resource_type": "portatil",
        "resource_model": "R2022",
        "resource_state": "free"
    }

    def test_resource_create(self):
        dato = requests.post(ResourceTest.URI, json=ResourceTest.OBJECT_VALUE)
        self.assertEqual(dato.status_code, 200)

    def test_resource_read_all(self):
        dato = requests.get(ResourceTest.URI)
        self.assertEqual(dato.status_code, 200)
        self.assertEqual(len(dato.json()), 7)

    def test_resource_search_name(self):
        resource_name = "Notebook2002"
        dato = requests.get("{}/{}".format(ResourceTest.BOOK_URI, resource_name))
        self.assertEqual(dato.status_code, 200)
        self.assertDictEqual(dato.json(), ResourceTest.OBJECT_VALUE)



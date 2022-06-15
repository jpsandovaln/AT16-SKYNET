import connexion
import six

from swagger_server.models.success_face_recognition_post import SuccessFaceRecognitionPost  # noqa: E501
from swagger_server import util


def update_face_with_form(file, person):  # noqa: E501
    """Search an object

     # noqa: E501

    :param file: Zip file
    :type file: werkzeug.datastructures.FileStorage
    :param person: Image of person face to search
    :type person: werkzeug.datastructures.FileStorage

    :rtype: SuccessFaceRecognitionPost
    """
    return 'do some magic!'

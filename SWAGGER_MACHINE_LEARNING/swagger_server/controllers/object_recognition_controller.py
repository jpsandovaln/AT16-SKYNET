import connexion
import six

from swagger_server.models.success_object_recognition_post import SuccessObjectRecognitionPost  # noqa: E501
from swagger_server import util


def update_object_with_form(file, name, model, percentage):  # noqa: E501
    """Search an object

     # noqa: E501

    :param file: file of pictures
    :type file: werkzeug.datastructures.FileStorage
    :param name: Name of the object to search
    :type name: str
    :param model: ModelVgg16, InceptionV3, Resnet
    :type model: str
    :param percentage: Percentage between 0-1
    :type percentage: float

    :rtype: SuccessObjectRecognitionPost
    """
    return 'do some magic!'

import connexion
import six

from swagger_server.models.success_emotion_post import SuccessEmotionPost  # noqa: E501
from swagger_server import util


def update_emotion_with_form(file):  # noqa: E501
    """Recognize a face emotion

     # noqa: E501

    :param file: Image file
    :type file: werkzeug.datastructures.FileStorage

    :rtype: SuccessEmotionPost
    """
    return 'do some magic!'

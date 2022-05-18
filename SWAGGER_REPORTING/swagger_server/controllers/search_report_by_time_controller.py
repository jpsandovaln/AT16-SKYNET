import connexion
import six

from swagger_server.models.success_gender_post import SuccessGenderPost  # noqa: E501
from swagger_server import util


def update_gender_with_form(open_time, close_time):  # noqa: E501
    """Search the number of reservations made in the morning and afternoon for each gender

     # noqa: E501

    :param open_time: HH:MM:SS eg. 08:30:00
    :type open_time: str
    :param close_time: HH:MM:SS eg. 18:30:00
    :type close_time: str

    :rtype: SuccessGenderPost
    """
    return 'do some magic!'

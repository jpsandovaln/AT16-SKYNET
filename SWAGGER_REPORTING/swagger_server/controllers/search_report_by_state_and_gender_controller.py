import connexion
import six

from swagger_server.models.success_post import SuccessPost  # noqa: E501
from swagger_server import util


def update_state_with_form(state, person_gender):  # noqa: E501
    """Search report by state and gender

     # noqa: E501

    :param state: String eg. new
    :type state: str
    :param person_gender: M or F
    :type person_gender: str

    :rtype: SuccessPost
    """
    return 'do some magic!'

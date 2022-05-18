import connexion
import six

from swagger_server.models.success_post import SuccessPost  # noqa: E501
from swagger_server import util


def update_ageand_gender_with_form(person_age, person_gender):  # noqa: E501
    """Search report by age and gender

     # noqa: E501

    :param person_age: Integer eg. 55
    :type person_age: int
    :param person_gender: M or F
    :type person_gender: str

    :rtype: SuccessPost
    """
    return 'do some magic!'

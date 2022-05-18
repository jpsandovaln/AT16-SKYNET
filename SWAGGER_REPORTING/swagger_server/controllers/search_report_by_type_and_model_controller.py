import connexion
import six

from swagger_server.models.success_post import SuccessPost  # noqa: E501
from swagger_server import util


def update_report_type_with_form(type, model):  # noqa: E501
    """Search report by type and model

     # noqa: E501

    :param type: String eg. Asus
    :type type: str
    :param model: String eg. Jeep
    :type model: str

    :rtype: SuccessPost
    """
    return 'do some magic!'

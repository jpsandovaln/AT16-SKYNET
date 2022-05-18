import connexion
import six

from swagger_server.models.success_country_post import SuccessCountryPost  # noqa: E501
from swagger_server import util


def update_country_with_form(start_date, end_date):  # noqa: E501
    """Search the number of reservations for each country within a range of dates

     # noqa: E501

    :param start_date: MM/DD/YYYY eg. 01/18/1995
    :type start_date: str
    :param end_date: MM/DD/YYYY eg. 01/18/2019
    :type end_date: str

    :rtype: SuccessCountryPost
    """
    return 'do some magic!'

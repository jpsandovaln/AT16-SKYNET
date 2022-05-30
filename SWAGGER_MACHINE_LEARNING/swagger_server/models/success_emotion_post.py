#
# @success_emotion_post.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# Edificio Union № 1376 Av. General Inofuentes esquina Calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object4 import Object4
from swagger_server import util


class SuccessEmotionPost(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, url: Object4=None):  # noqa: E501
        """SuccessEmotionPost - a model defined in Swagger

        :param url: The url of this SuccessEmotionPost.  # noqa: E501
        :type url: Object4
        """
        self.swagger_types = {
            'url': Object4
        }

        self.attribute_map = {
            'url': 'URL'
        }

        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'SuccessEmotionPost':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SuccessEmotionPost of this SuccessEmotionPost.  # noqa: E501
        :rtype: SuccessEmotionPost
        """
        return util.deserialize_model(dikt, cls)

    @property
    def url(self) -> Object4:
        """Gets the url of this SuccessEmotionPost.


        :return: The url of this SuccessEmotionPost.
        :rtype: Object4
        """
        return self._url

    @url.setter
    def url(self, url: Object4):
        """Sets the url of this SuccessEmotionPost.


        :param url: The url of this SuccessEmotionPost.
        :type url: Object4
        """

        self._url = url

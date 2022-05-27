#
# @object4.py Copyright (c) 2022 Jalasoft.
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
from swagger_server import util


class Object4(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, http127_0_0_15000downloadersaved_filescompress_files: str=None):  # noqa: E501
        """Object4 - a model defined in Swagger

        :param http127_0_0_15000downloadersaved_filescompress_files: The http127_0_0_15000downloadersaved_filescompress_files of this Object4.  # noqa: E501
        :type http127_0_0_15000downloadersaved_filescompress_files: str
        """
        self.swagger_types = {
            'http127_0_0_15000downloadersaved_filescompress_files': str
        }

        self.attribute_map = {
            'http127_0_0_15000downloadersaved_filescompress_files': 'http://127.0.0.1:5000/downloader/saved_files/compress_files/'
        }

        self._http127_0_0_15000downloadersaved_filescompress_files = http127_0_0_15000downloadersaved_filescompress_files

    @classmethod
    def from_dict(cls, dikt) -> 'Object4':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Object4 of this Object4.  # noqa: E501
        :rtype: Object4
        """
        return util.deserialize_model(dikt, cls)

    @property
    def http127_0_0_15000downloadersaved_filescompress_files(self) -> str:
        """Gets the http127_0_0_15000downloadersaved_filescompress_files of this Object4.


        :return: The http127_0_0_15000downloadersaved_filescompress_files of this Object4.
        :rtype: str
        """
        return self._http127_0_0_15000downloadersaved_filescompress_files

    @http127_0_0_15000downloadersaved_filescompress_files.setter
    def http127_0_0_15000downloadersaved_filescompress_files(self, http127_0_0_15000downloadersaved_filescompress_files: str):
        """Sets the http127_0_0_15000downloadersaved_filescompress_files of this Object4.


        :param http127_0_0_15000downloadersaved_filescompress_files: The http127_0_0_15000downloadersaved_filescompress_files of this Object4.
        :type http127_0_0_15000downloadersaved_filescompress_files: str
        """

        self._http127_0_0_15000downloadersaved_filescompress_files = http127_0_0_15000downloadersaved_filescompress_files

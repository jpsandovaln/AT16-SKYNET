#
# @object_result.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Condidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#


class ObjectResult:
    """Class that represent the return of Model"""
    def __init__(self, name="", percentage=0, path_file="//"):
        """Constructor of ObjectResult"""
        self._name = name
        self._percentage = percentage
        self._path_file = path_file
        self._id_object = ''

    # Return the name of the result
    def get_name(self):
        return self._name

    # Set tne name of the result
    def set_name(self, name):
        self._name = name

    # Return the percentage of the result
    def get_percentage(self):
        return self._percentage

    # Set the percentage of the result
    def set_percentage(self, percentage):
        self._percentage = percentage

    # Return the path of the file of the result
    def get_path_file(self):
        return self._path_file

    # Set the path of the file of the result
    def set_path_file(self, path_file):
        self._path_file = path_file

    # Return the id of the Result
    def get_id_object(self):
        return self._id_object

    # Set the id of the result
    def set_id_object(self, id_object):
        self._id_object = id_object

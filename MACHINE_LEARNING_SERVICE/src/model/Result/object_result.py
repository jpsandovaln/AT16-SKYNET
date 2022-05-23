#
# @object_result.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#


class ObjectResult:
    """Class that represent the return of Model"""
    def __init__(self, name: str = "", percentage: float = 0, path_file: str = "//"):
        """Constructor of ObjectResult"""
        self._name: str = name
        self._percentage: float = percentage
        self._path_file: str = path_file
        self._id_object: str = ''

    # Return the name of the result
    def get_name(self) -> str:
        return self._name

    # Set tne name of the result
    def set_name(self, name: str):
        self._name = name

    # Return the percentage of the result
    def get_percentage(self) -> float:
        return self._percentage

    # Set the percentage of the result
    def set_percentage(self, percentage: float):
        self._percentage = percentage

    # Return the path of the file of the result
    def get_path_file(self) -> str:
        return self._path_file

    # Set the path of the file of the result
    def set_path_file(self, path_file: any):
        self._path_file = path_file

    # Return the id of the Result
    def get_id_object(self) -> str:
        return self._id_object

    # Set the id of the result
    def set_id_object(self, id_object: str):
        self._id_object = id_object

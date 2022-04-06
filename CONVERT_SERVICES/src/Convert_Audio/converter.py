#
# @converter.py Copyright (c)
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

class Converter:
    def __init__(self, str_input, path_in, path_out):
        self.path_in = path_in
        self.path_out = path_out
        self.str_input = str_input

    def get_str_input(self):
        return self.str_input

    def get_path_in(self):
        return self.path_in

    def get_path_out(self):
        return self.path_out


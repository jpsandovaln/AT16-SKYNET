#
# test_convertor.py Copyright (c) 2022 Jalasoft.
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

import unittest
from src.model.convertor import Convertor
from unittest.mock import patch
from unittest.mock import Mock


class TestConvertor(unittest.TestCase):

    def test_convertor(self):
        mock_get_patcher = patch('instructions.request.post')
        instructions = [{
            "input_file": "Text"
        }]
        mock_get = mock_get_patcher.start()
        mock_get.return_value = Mock()
        convertor = Convertor('', '')
        result = convertor.get_input_file()
        self.assertEqual('saved_files/', result)

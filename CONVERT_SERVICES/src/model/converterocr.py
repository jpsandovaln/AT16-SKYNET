#
# @converter_ocr.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
#1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
#All rights reserved.
#
#This software is the confidential and proprietary information of
#Jalasoft, ("Condidential Information"). You shall # not
#disclose such Confidential Information and shall use it only in
#accordance with the terms of the license agreement you entered into
#with Jalasoft.
#

import pytesseract as tesseract_converter
from PIL import Image
from src.model.convertor import Convertor


class ConvertOCR(Convertor):
    def __init__(self, input_data, input_file):
        super().__init__(input_data, input_file)
        self.instructions = self.getInstructions()

    def Exec(self):
        language = self.instructions.values.get('language')

        exe_location = r'../../third_party/win/tesseract/tesseract'
        tesseract_converter.pytesseract.tesseract_cmd = exe_location

        image_to_text = Image.open(self.input_file)
        text_result = tesseract_converter.image_to_string(image_to_text, lang=language)

        output_file = open(self.output_file + '/' + self.name_output, 'w', encoding="utf-8")
        output_file.write(text_result + '\n')
        output_file.close()

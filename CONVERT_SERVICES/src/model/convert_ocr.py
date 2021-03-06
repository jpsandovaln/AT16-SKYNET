#
# @converter_ocr.py Copyright (c)
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

import cv2
import pytesseract as tesseract_converter
from src.model.convertor import Convertor
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from docx import Document


class ConvertOCR(Convertor):
    # Constructor
    def __init__(self, input_data: str, input_file: str):
        super().__init__(input_data, input_file)
        self.instructions: str = self.get_instructions()

    # Converts image to string
    def text_result(self) -> tesseract_converter:
        language: str = self.instructions.values.get('language')

        # the executeble path was deleted, because now tesseract is consumed directly once it is installed in the docker container
        image_to_text = cv2.imread(self.input_file)
        text_result2: tesseract_converter = tesseract_converter.image_to_string(image_to_text, lang=language)
        return text_result2

    # Converts string to pdf or docx or txt
    def exec(self):
        # Environment variables
        # load_dotenv()
        pdf_format: str = 'pdf'
        docx_format: str = 'docx'
        txt_format: str = 'txt'

        output_format: str = self.instructions.values.get('format')
        text_result: tesseract_converter = self.text_result()

        if output_format == txt_format:
            output_file: str = open(self.output_file + '/' + self.name_output, 'w', encoding="utf-8")
            output_file.write(text_result + '\n')
            output_file.close()

        elif output_format == pdf_format:
            width, height = A4
            pdf_document: canvas = canvas.Canvas(self.output_file + '/' + self.name_output, pagesize=A4)
            text: pdf_document = pdf_document.beginText(50, height - 50)
            text.textLines(text_result)
            pdf_document.drawText(text)
            pdf_document.showPage()
            pdf_document.save()

        elif output_format == docx_format:
            document: any = Document()
            document.add_paragraph(text_result)
            document.save(self.output_file + '/' + self.name_output)
        else:
            pass



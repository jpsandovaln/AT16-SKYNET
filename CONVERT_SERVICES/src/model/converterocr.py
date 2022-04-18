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


import pytesseract as tesseract_converter
from PIL import Image
from src.model.convertor import Convertor
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from docx import Document
import os
from dotenv import load_dotenv


class ConvertOCR(Convertor):
    # Constructor
    def __init__(self, input_data, input_file):
        super().__init__(input_data, input_file)
        self.instructions = self.getInstructions()

    # Convert image to string
    def text_result(self):
        language = self.instructions.values.get('language')

        # Executable path
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        TESSERACT_PATH = os.path.join(ROOT_DIR, 'third_party', 'win', 'tesseract', 'tesseract')
        tesseract_converter.pytesseract.tesseract_cmd = TESSERACT_PATH

        image_to_text = Image.open(self.input_file)
        text_result = tesseract_converter.image_to_string(image_to_text, lang=language)
        return text_result

    # Convert string to pdf or docx or txt
    def Exec(self):
        # Environment variables
        load_dotenv()
        pdf_format = os.getenv('PDF_FORMAT')
        docx_format = os.getenv('DOCX_FORMAT')
        txt_format = os.getenv('TXT_FORMAT')

        output_format = self.instructions.values.get('format')
        text_result = self.text_result()

        if output_format == txt_format:
            output_file = open(self.output_file + '/' + self.name_output, 'w', encoding="utf-8")
            output_file.write(text_result + '\n')
            output_file.close()

        elif output_format == pdf_format:
            w, h = A4
            pdf_document = canvas.Canvas(self.output_file + '/' + self.name_output, pagesize=A4)
            text = pdf_document.beginText(50, h - 50)
            text.textLines(text_result)
            pdf_document.drawText(text)
            pdf_document.showPage()
            pdf_document.save()

        elif output_format == docx_format:
            document = Document()
            document.add_paragraph(text_result)
            document.save(self.output_file + '/' + self.name_output)
        else:
            print('error')

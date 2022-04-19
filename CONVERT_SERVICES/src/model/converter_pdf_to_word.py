#
# @converter_pdf_to_word.py Copyright (c)
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


import win32com.client
import os
archivo = 'Test.pdf'
word = win32com.client.Dispatch("word.Application")
word.visible = 0

doc_pdf = archivo.get_name()
input_file = os.path.abspath(doc_pdf)

wb = word.Documents.Open(input_file)
output_file = os.path.abspath(doc_pdf[0:-4] + "docx".format())
wb.SaveAs2(output_file, FileFormat=16)
print("pdf to Docx is completed")
wb.Close()

word.Quit()
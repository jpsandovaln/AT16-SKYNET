
#
# @object_result.py Copyright (c)
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

from src.convert.convertimage import ConvertImage


prueba = ConvertImage('color=RGB,widht=100,rotate=180,MirrorVert','C:\dos\mac.png','C:\dres','tiff')
prueba.Exec()
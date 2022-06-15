#
# @Dockerfile Copyright (c)
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

# import linux sytem operating, alpine 3.10
FROM python:3.8.5-slim-buster

# Run the apk to add a new package python3 with pip, and update pip3
RUN apt update && apt upgrade -y
RUN apt install -y imagemagick
RUN apt install tesseract-ocr -y
RUN apt-get install tesseract-ocr-spa -y
RUN apt install python3-opencv -y
RUN apt install -y libimage-exiftool-perl
RUN apt-get install -y ffmpeg
# RUN apt add --no-cache python3-dev \
#    && pip3 install --upgrade pip
# Set the work directory
WORKDIR /app

# Copy all files to app directory
COPY . /app

# Run requirements to install all packages

RUN pip install -r requirements.txt

# Execute python3 and main.py
CMD ["python3", "main.py"]
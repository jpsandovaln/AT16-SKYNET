#
# @Dockerfile Copyright (c)
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

FROM python:3.7.3-stretch

# Install libgl1 openCV
RUN apt-get update
RUN apt install -y libgl1-mesa-glx
# Set the work directory
WORKDIR /app
# Copy all files to app directory
COPY . /app
RUN python -m pip install --upgrade pip
# Run requirements to install all packages
RUN pip install -r requirements.txt
# Change the import name of the keras-vggface
RUN python rename_file.py

CMD ["python3", "main.py"]

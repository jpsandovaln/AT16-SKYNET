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

# import linux sytem operating, jupyter
FROM jupyter/scipy-notebook
#FROM jupyter/datascience-notebook
#for enable the sudo commands
USER root
ENV GRANT_SUDO: "yes"

# Run the apk to add a new package joblib
RUN pip3 install joblib

# Set the work directory
WORKDIR /app

# Copy all files to app directory
COPY . /app

# Run requirements to install all packages
RUN pip3 install tensorflow
RUN pip3 install G6-iris-recognition
RUN pip3 install keras==2.8.0
RUN pip3 install python-decouple
RUN pip3 install vggface
RUN pip3 install mtcnn
RUN pip3 install Keras-Applications==1.0.8
RUN pip3 install Keras-Preprocessing==1.1.2
RUN pip3 --no-cache-dir install -r requirements.txt

RUN cp /app/src/model/vggface_patch/models.py /opt/conda/lib/python3.9/site-packages/keras_vggface/models.py

# Execute python3 and main.py
CMD ["python3", "main.py"]
FROM python:3.8.5-slim-buster

# Set the work directory
WORKDIR /app

# Copy all files to app directory
COPY . /app

# Run requirements to install all packages
RUN pip install -r requirements.txt

# Execute main.py
ENTRYPOINT python main.py
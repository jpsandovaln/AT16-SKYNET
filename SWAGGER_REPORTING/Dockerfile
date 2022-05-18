FROM python:3-alpine

# Set the work directory
WORKDIR /app

# Copy all files to app directory
COPY . /app

# Run requirements to install all packages
RUN pip3 --no-cache-dir install -r requirements.txt

COPY . /usr/src/app

EXPOSE 6005

# Execute main.py
CMD ["python3", "__main__.py"]
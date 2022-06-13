FROM python:3.6-alpine

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 6004

CMD ["python3", "__main__.py"]
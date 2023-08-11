#FROM balenalib/raspberrypi4-64-debian:latest
FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y python3-pip
RUN python3 -m pip install balena-sdk

COPY . /app

WORKDIR /app

RUN pip3 freeze > requirements.txt
RUN pip3 install -r requirements.txt

RUN cat requirements.txt

#CMD python3 getvars.py



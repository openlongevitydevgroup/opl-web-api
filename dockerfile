FROM python:latest 

ENV PYTHONUNBUFFERED 1

ENV DockerHome = /home/backend

RUN mkdir /backend 

WORKDIR /backend 

ADD . /backend/ 

RUN pip install -r requirements.txt


FROM python:3.11.1

ENV PYTHONUNBUFFERED 1

ENV DockerHome = /home/backend

RUN mkdir /backend 

WORKDIR /backend 

ADD . /backend/ 
RUN pip install -r requirements.txt




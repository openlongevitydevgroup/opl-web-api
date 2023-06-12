FROM python:3.11.1

ENV PYTHONUNBUFFERED 1

ENV DockerHome = /home/backend

RUN mkdir /backend 

WORKDIR /backend 

ADD . /backend/ 

RUN apk add --update postgresql-client jpeg-dev
RUN apk add --update --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN pip install -r requirements.txt



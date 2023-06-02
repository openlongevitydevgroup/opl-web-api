FROM python:latest 

ENV DockerHome = /home/backend

RUN mkdir -p ${DockerHome}

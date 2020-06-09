FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN mkdir /main
WORKDIR /main
COPY . /main/
RUN pip3 install -r requirements.txt





# syntax=docker/dockerfile:1

FROM python:latest

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update 
RUN apt-get -y upgrade
RUN apt-get install nano

COPY app.py .
COPY requirements.txt .




CMD tail -f /dev/null

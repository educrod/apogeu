# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.7-buster

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/apogeu

RUN pip --proxy=http://189.125.185.46:3128 install --upgrade pip
RUN pip --proxy=http://189.125.185.46:3128 install pipenv
COPY ./Pipfile /usr/src/apogeu/Pipfile
ENV http_proxy http://189.125.185.46:3128
ENV https_proxy http://189.125.185.46:3128
RUN pipenv install --skip-lock --system

# copy project
COPY ./app/local_settings.py /etc/apogeu/local_settings.py
COPY . /usr/src/apogeu

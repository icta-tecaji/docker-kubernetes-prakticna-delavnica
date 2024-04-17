# syntax=docker/dockerfile:1

# pull official base image
FROM python:3.11.9-slim-bookworm

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies for easier debugging
RUN apt update && apt install -y curl

# install uv package manager
ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod -R 655 /install.sh && /install.sh && rm /install.sh

# install python dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt
COPY ./requirements_dev.txt /usr/src/app/requirements_dev.txt
COPY ./requirements_test.txt /usr/src/app/requirements_test.txt
RUN /root/.cargo/bin/uv pip install --system --no-cache -r /usr/src/app/requirements_dev.txt

# copy project
COPY . /usr/src/app

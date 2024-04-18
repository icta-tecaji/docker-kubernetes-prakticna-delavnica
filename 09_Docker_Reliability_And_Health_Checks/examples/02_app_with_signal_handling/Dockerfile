# syntax=docker/dockerfile:1

FROM python:3.11.9-slim-bookworm

ADD . /code
WORKDIR /code
ENTRYPOINT ["python", "-u", "app.py"]

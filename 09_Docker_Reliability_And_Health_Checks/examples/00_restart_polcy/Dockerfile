FROM python:3.9-slim
RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*
ADD . /code
WORKDIR /code
ENTRYPOINT ["python3", "-u", "/code/app.py"]

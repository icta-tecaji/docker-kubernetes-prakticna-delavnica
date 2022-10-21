FROM python:3.9-slim
RUN apt-get update && apt-get install -y procps netcat && rm -rf /var/lib/apt/lists/*
ADD . /code
WORKDIR /code
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]

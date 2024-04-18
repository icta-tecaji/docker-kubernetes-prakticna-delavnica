FROM python:3.9-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

ENV RND_API_HOST_AND_PORT=rnd-api:5000

CMD ["python", "app.py"]

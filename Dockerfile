# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.7
COPY . /app
WORKDIR /app
RUN apt-get update
RUN pip install -r requirements.txt
CMD python -m flask run
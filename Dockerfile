
FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
# RUN apk update
# RUN apk add mongodb





RUN mkdir /src
WORKDIR /src
COPY ./src /src

RUN adduser -D user
USER user

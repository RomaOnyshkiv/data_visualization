FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /data_visualization

WORKDIR /data_visualization

ADD . /data_visualization/

RUN pip install -r requirements.txt

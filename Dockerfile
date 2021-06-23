FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /data_visualization

WORKDIR /data_visualization

ADD . /data_visualization/

RUN pip3 install -r requirements.txt

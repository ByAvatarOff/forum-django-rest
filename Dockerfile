FROM python:3.6-alpine

RUN mkdir /dockerDRF
WORKDIR /dockerDRF

ADD req.txt /dockerDRF/

RUN pip install --upgrade pip
RUN pip install -r req.txt

ADD . /dockerDRF/

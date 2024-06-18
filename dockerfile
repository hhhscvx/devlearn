FROM python:3.11

COPY requirements.txt /temp/requirements.txt

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password devlearner

COPY devlearn /devlearn
WORKDIR /devlearn
EXPOSE 8000

USER devlearner

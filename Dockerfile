FROM python:3.8-slim-buster 
ENV PYTHONNUNBUFFERED=1

WORKDIR /skakey_pos

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt 


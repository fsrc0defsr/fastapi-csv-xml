FROM python:3.10.12

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./instantclient-basic-linux.x64-21.13.0.0.0dbru.zip /tmp/
COPY ./instantclient-sdk-linux.x64-21.13.0.0.0dbru.zip /tmp/

RUN apt-get update && \
    apt-get install -y unzip libaio1 libaio-dev && \
    unzip /tmp/instantclient-basic-linux.x64-21.13.0.0.0dbru.zip -d /usr/local/ && \
    unzip /tmp/instantclient-sdk-linux.x64-21.13.0.0.0dbru.zip -d /usr/local/ && \
    ln -s /usr/local/instantclient_21_13 /usr/local/instantclient && \
    rm /tmp/instantclient-basic-linux.x64-21.13.0.0.0dbru.zip /tmp/instantclient-sdk-linux.x64-21.13.0.0.0dbru.zip && \
    echo "/usr/local/instantclient" > /etc/ld.so.conf.d/instantclient.conf && \
    ldconfig && \
    chmod 755 /usr/local/instantclient/libclntsh.so.*

COPY . /app

RUN pip install -r requirements.txt

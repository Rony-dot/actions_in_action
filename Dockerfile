FROM ubuntu:24.04

RUN apt-get update -y && apt-get upgrade -y && useradd -m docker

RUN apt-get install -y --no-install-recommends \
    curl wget vim tar python3 python3-pip

WORKDIR /app

COPY requirements.txt .
# RUN chown -R 777 ./
# RUN echo $(ls -ltrh *) && sleep 10s
# RUN python3 -m venv /app/venv
# RUN source /app/venv/bin/activate
RUN pip3 install -r requirements.txt --break-system-packages

COPY src/ /app/
COPY .env /app/
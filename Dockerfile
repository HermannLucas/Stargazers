FROM debian:stable-slim
WORKDIR /app

RUN apt-get update -qy && apt-get install -y python3 python3-pip

COPY ./. /app
RUN pip install -r /app/requirements.txt

ENTRYPOINT flask --app main run

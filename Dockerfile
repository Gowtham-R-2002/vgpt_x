FROM python:3.10.0-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y portaudio19-dev

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD python ./app.py



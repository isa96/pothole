FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 libopencv-dev git build-essential -y
RUN pip install gdown

RUN pip install flask

COPY . .

RUN chmod +x init_app.sh
RUN ./init_app.sh

EXPOSE 8080

CMD [ "python3", "app.py" ]

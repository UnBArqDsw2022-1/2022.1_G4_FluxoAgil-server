FROM python:3.10-slim

WORKDIR /fluxoagil
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 libpq-dev gcc python3-opencv -y
RUN pip install -r requirements.txt

COPY . /fluxoagil
RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "scripts/start.sh"]

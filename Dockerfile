FROM python:3.10-slim

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 libpq-dev gcc -y

WORKDIR /fluxoagil

COPY . /fluxoagil
RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "scripts/start.sh"]

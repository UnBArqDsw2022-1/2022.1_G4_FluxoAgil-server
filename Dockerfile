FROM python:3.8-slim-buster

COPY requirements.txt ./requirements.txt
COPY main.py ./main.py
COPY fluxoagil /fluxoagil

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]
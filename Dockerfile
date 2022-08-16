FROM python:3.10-slim

WORKDIR /usr/src/app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY main.py ./main.py
COPY fluxoagil fluxoagil

EXPOSE 5000

CMD ["python3", "main.py"]
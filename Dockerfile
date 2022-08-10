FROM python:3.8

COPY requeriments.txt ./requeriments.txt
COPY main.py ./main.py
COPY fluxoagil /fluxoagil

RUN pip install -r requeriments.txt

CMD ["python", "./main.py"]
FROM python:3.11-slim-buster

WORKDIR /py-http-call

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY templates ./templates/
COPY app.py .

CMD [ "python3", "app.py"]
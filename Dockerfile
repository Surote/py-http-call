FROM registry.access.redhat.com/ubi9/python-311:1-34

WORKDIR /py-http-call

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY templates ./templates/
COPY app.py .

CMD [ "python3", "app.py"]
FROM registry.access.redhat.com/ubi9/python-312:9.6-1747333115

WORKDIR /py-http-call

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY templates ./templates/
COPY app.py .

CMD [ "python3", "app.py"]
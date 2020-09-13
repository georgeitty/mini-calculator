FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install flask
CMD python ./calc.py


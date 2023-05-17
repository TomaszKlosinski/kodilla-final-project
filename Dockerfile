FROM python:3.11

COPY . /app/

WORKDIR /app

ENV FLASK_APP=blog.py

RUN pip install --no-cache -r requirements.txt
CMD flask run --host 0.0.0.0

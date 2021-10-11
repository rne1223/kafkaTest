FROM python:3.7-slim-buster

COPY . .

RUN pip install -r requirements.txt

EXPOSE 30001
WORKDIR /app

CMD python app.py 
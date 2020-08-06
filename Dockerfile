FROM python:3.8-slim

WORKDIR /usr/src/app

COPY ./app/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/ .

RUN mkdir -p sentry

CMD ["python", "main.py"]


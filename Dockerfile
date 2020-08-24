FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/ ./app/

RUN mkdir -p sentry

ENV PORT=80
EXPOSE 80

CMD ["python", "-m", "app"]


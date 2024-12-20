FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache git postgresql-dev gcc libc-dev
RUN apk add --no-cache gcc g++ make libffi-dev python3-dev build-base

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ARG email=superuser@oppositionus.com
ENV DJANGO_SUPERUSER_EMAIL=${email}

ARG password=superuser
ENV DJANGO_SUPERUSER_PASSWORD=${password}

RUN python3 ./manage.py migrate

RUN python3 ./manage.py populate

RUN python3 ./manage.py createsuperuser --noinput

ENTRYPOINT python3 ./manage.py runserver 0.0.0.0:8000
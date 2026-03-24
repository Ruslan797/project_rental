#FROM python:3.12-slim
## Die  Systemabhängigkeiten werden installiert
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    build-essential \
#    libmariadb-dev-compat \
#    pkg-config \
#    && rm -rf /var/lib/apt/lists/*
#
## Die  Python-Abhängigkeiten werden installiert
#WORKDIR /app
#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt
#
## Die restlichen Daten werden kopiert
#COPY . .
#
## Die statischen Dataien werden gesamelt
#RUN python manage.py collectstatic --noinput
#
## Gunicorn wird gestartet
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]

FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    libmariadb-dev-compat \
    pkg-config \
    curl \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .
# collectstatic
RUN python manage.py collectstatic --noinput
# gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]



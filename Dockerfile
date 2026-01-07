## Используем официальный образ Python
#FROM python:3.11-slim
#
## Устанавливаем зависимости
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    build-essential \
#    libmysqlclient-dev \
#    && rm -rf /var/lib/apt/lists/*
#
## Устанавливаем Poetry (если используете)
#RUN pip install poetry
#
## Копируем файлы проекта
#WORKDIR /app
#COPY . .
#
## Устанавливаем зависимости Python
#RUN pip install --no-cache-dir -r requirements.txt
#
## Собираем статические файлы (если нужно)
## RUN python manage.py collectstatic --noinput

# Запускаем сервер
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Используем официальный образ Python 3.13
#FROM python:3.13-slim
#
## Устанавливаем системные зависимости
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    build-essential \
#    libmariadb-dev-compat \
#    pkg-config \
#    && rm -rf /var/lib/apt/lists/*
#
## Копируем файлы проекта
#WORKDIR /app
#COPY . .
#
## Устанавливаем зависимости из requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt
#
## Запускаем Django-сервер
## CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]

FROM python:3.12-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libmariadb-dev-compat \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости Python
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Собираем статические файлы
RUN python manage.py collectstatic --noinput

# Запускаем Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]



FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV DJANGO_SETTINGS_MODULE=auth_service.settings
CMD ["gunicorn", "auth_service.wsgi:application", "--bind", "0.0.0.0:8000"]
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV PYTHONPATH=/app:/app/app
EXPOSE 8001
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
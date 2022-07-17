FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1

# Write the directory where manage.py is located
WORKDIR /auction

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# RUN postgres psql

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
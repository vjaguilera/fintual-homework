FROM python:3.8-slim

## create directories
RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

# main run
CMD ["python", "main.py"]
# syntax=docker/dockerfile:1
FROM python as base

WORKDIR /chatsky_pipeline

COPY requirements.txt requirements.txt
RUN ["python", "-m", "pip", "install", "-r", "requirements.txt"]

COPY bot ./bot
COPY __init__.py .

FROM base as test
COPY test.py .
COPY test_data.json .
RUN ["python", "-m", "pytest", "test.py"]

FROM base as development
COPY app.py .
CMD ["python", "app.py"]

FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN python3 -m pip install --no-cache-dir --progress-bar off flask==2.2.5

EXPOSE 8888

CMD ["python3", "sample_app.py"]

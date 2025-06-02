FROM python:3.11-slim

WORKDIR /app

COPY app /app/app
COPY tests /app/tests
COPY run_tests.sh .
COPY requirements.txt .
COPY build_docker.sh .

RUN pip install -r requirements.txt

CMD ["./run_tests.sh"]

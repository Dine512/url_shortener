FROM python:3.11-alpine

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8080"]
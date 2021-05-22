FROM python:3.8

WORKDIR /app
COPY . /app

RUN python3 -m pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "pycoder.api.app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
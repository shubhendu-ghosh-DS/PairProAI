FROM python:3.10

WORKDIR /app

COPY requirements.txt .
COPY app/ app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]

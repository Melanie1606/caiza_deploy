FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 1001

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

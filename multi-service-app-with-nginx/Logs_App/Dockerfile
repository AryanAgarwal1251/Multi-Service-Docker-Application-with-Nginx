FROM python:3.10-slim

WORKDIR /app

# Correct pip index-url syntax without markdown brackets
COPY requirements.txt .
RUN pip install --no-cache-dir --default-timeout=1000 -r requirements.txt --index-url https://pypi.org/simple

COPY . .

EXPOSE 6000

CMD ["python", "app.py"]

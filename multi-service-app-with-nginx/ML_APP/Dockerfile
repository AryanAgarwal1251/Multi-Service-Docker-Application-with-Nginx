FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Correct pip index URL syntax without markdown formatting
RUN pip install --no-cache-dir --default-timeout=1000 -r requirements.txt --index-url https://pypi.org/simple

# Download VADER lexicon for nltk
RUN python -m nltk.downloader vader_lexicon

COPY . .

EXPOSE 5000

CMD ["python", "self_api.py"]

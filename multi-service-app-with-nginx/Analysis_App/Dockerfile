FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive \
    MPLBACKEND=Agg

WORKDIR /app

# Install minimal system deps for headless matplotlib rendering
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --default-timeout=1000 -r requirements.txt --index-url https://pypi.org/simple

COPY . .

EXPOSE 5050

CMD ["python", "analysis.py"]

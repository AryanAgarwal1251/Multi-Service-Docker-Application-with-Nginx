FROM python:3.9-slim

WORKDIR /app
COPY . .

# Use plain index URL; optionally add --no-cache-dir and a generous timeout
RUN pip install --no-cache-dir --default-timeout=1000 -r requirements.txt --index-url https://pypi.org/simple

# Expose the port Streamlit actually binds to
EXPOSE 8501

# Start Streamlit bound to 0.0.0.0 so it’s reachable by NGINX and other containers
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

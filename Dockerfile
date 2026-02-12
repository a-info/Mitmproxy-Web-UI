# Dockerfile for MITM Proxy Web UI on Railway
# Uses start_mitm.py for dynamic PORT configuration

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install mitmproxy
RUN pip install --no-cache-dir mitmproxy==10.1.5

# Create directory for mitmproxy data
RUN mkdir -p /root/.mitmproxy

# Copy the start script
COPY start_mitm.py /app/

# Expose proxy port (web UI port is dynamic via $PORT)
EXPOSE 8080

# Start using python script which reads PORT env variable
CMD ["python3", "/app/start_mitm.py"]

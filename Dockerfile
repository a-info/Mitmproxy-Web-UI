# Dockerfile for MITM Proxy Web UI on Realway.com
# This builds and runs mitmproxy with default mitmweb interface

FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install mitmproxy
RUN pip install --no-cache-dir mitmproxy==10.1.5

# Create directory for mitmproxy data
RUN mkdir -p /root/.mitmproxy

# Expose proxy port and web UI port
EXPOSE 8080 8081

# Set environment variables
ENV MITMWEB_HOST=0.0.0.0
ENV MITMWEB_PORT=8081
ENV PROXY_PORT=8080

# Start mitmweb (proxy + web UI)
CMD mitmweb \
    --mode regular@0.0.0.0:8080 \
    --web-host 0.0.0.0 \
    --web-port 8081 \
    --no-web-open-browser \
    --ssl-insecure \
    --set confdir=/root/.mitmproxy

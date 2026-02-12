# MITM Proxy Web UI

HTTP/HTTPS traffic interception using official mitmproxy with default mitmweb interface.

## Features

- Real-time HTTP/HTTPS traffic interception
- Official mitmweb interface (default MITM proxy web UI)
- Docker support for realway.com deployment
- Easy local deployment

## Files

- `start_mitm.py` - Run locally without Docker
- `Dockerfile` - Docker image for realway.com
- `docker-compose.yml` - Local Docker deployment
- `Procfile` - Realway.com deployment config
- `requirements.txt` - Python dependencies
- `REALWAY_DEPLOY.md` - Detailed realway.com deployment guide

## Local Development

### Option 1: Python (without Docker)

```bash
pip install mitmproxy==10.1.5
python start_mitm.py
```

Access:
- Web UI: http://127.0.0.1:8081
- Proxy: 127.0.0.1:8080

### Option 2: Docker

```bash
docker-compose up
```

Access:
- Web UI: http://localhost:8081
- Proxy: localhost:8080

## Realway.com Deployment

See `REALWAY_DEPLOY.md` for detailed instructions.

Quick steps:
1. Go to [realway.com](https://realway.com)
2. Select "Deploy with Docker"
3. Upload this folder
4. Expose ports: 8080, 8081
5. Deploy

## Device Proxy Configuration

### Android/iOS:
1. Wi-Fi Settings → Proxy → Manual
2. Host: `your-server-ip` or realway URL
3. Port: `8080`

### Windows:
1. Settings → Network → Proxy
2. Address: `127.0.0.1` (local) or server IP
3. Port: `8080`

## HTTPS Certificate

For HTTPS sites, install certificate:
1. Go to `http://mitm.it` (with proxy enabled)
2. Download certificate for your device
3. Install and trust the certificate

## Important Notes

- **Security**: For educational and testing purposes only
- **Port 8080**: Proxy server
- **Port 8081**: Web UI (mitmweb)
- Realway.com deploy requires both ports exposed

## License

MIT License - For educational purposes only.

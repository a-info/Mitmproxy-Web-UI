# Realway.com Deployment Guide

## আপনার ফাইলগুলো (ইতিমধ্যে তৈরি):

- **Dockerfile** - Docker image তৈরির জন্য
- **docker-compose.yml** - Local test এর জন্য
- **Procfile** - Realway.com কীভাবে চালাবে তা বলে দেয়
- **requirements.txt** - mitmproxy ইনস্টলের জন্য
- **start_mitm.py** - লোকালে চালানোর জন্য

## Realway.com-এ Deploy করতে (Docker ব্যবহার করে):

### Step 1: Realway.com-এ যান
1. [realway.com](https://realway.com) এ লগইন করুন
2. "New Project" বা "Create App" তে ক্লিক করুন
3. **"Deploy with Docker"** সিলেক্ট করুন

### Step 2: ফোল্ডার আপলোড করুন
- "Upload Folder" সিলেক্ট করুন
- "mitm Proxy Web ui" ফোল্ডার আপলোড করুন
- **Dockerfile** auto-detect হবে

### Step 3: Port Configuration
**Exposed Ports:**
```
8080  # Proxy port
8081  # Web UI port
```

### Step 4: Deploy
"Deploy" বাটনে ক্লিক করুন।

### Step 5: Access করুন
Deploy সফল হলে realway.com URL দেবে:
- **Web UI:** `https://mitmproxy-web-ui.realway.com:8081`
- **Proxy:** `mitmproxy-web-ui.realway.com:8080`

## Local-এ Docker দিয়ে চালাতে:

```bash
docker-compose up
```

তারপর:
- **Web UI:** http://localhost:8081
- **Proxy:** localhost:8080

## Alternative: Python দিয়ে চালাতে (Docker ছাড়া)

```bash
pip install mitmproxy==10.1.5
python start_mitm.py
```

## Device Connect করতে:

Proxy configure করুন:
- **Host:** `mitmproxy-web-ui.realway.com` (বা local IP)
- **Port:** `8080`

Web UI দেখতে:
- `https://mitmproxy-web-ui.realway.com:8081` (realway)
- `http://localhost:8081` (local)

#!/usr/bin/env python3
"""
MITM Proxy Web UI - Railway Deployment
Uses official mitmweb interface
"""

import subprocess
import sys
import socket
import os

# Force unbuffered output for Railway logs
sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)

def find_free_port(start=8080, end=8090):
    """Find first available port in range"""
    for port in range(start, end):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port
    return None

def get_local_ip():
    """Get local network IP"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def main():
    # Check if running on Railway (has PORT environment variable)
    railway_port = os.getenv('PORT')
    
    if railway_port:
        # Railway deployment mode
        web_port = int(railway_port)
        # Use a different port for proxy, offset from web port
        proxy_port = web_port + 1000  # e.g., if web_port=8080, proxy=9080
        web_host = "0.0.0.0"  # Listen on all interfaces for Railway
        
        print("=" * 60)
        print("MITM Proxy Web UI - Railway Deployment")
        print("=" * 60)
        print()
        print(f"Web UI Port:    {web_port} (Railway assigned)")
        print(f"Proxy Port:     {proxy_port} (dynamic)")
        print(f"Web Host:       {web_host}")
        print("=" * 60)
        print()
    else:
        # Local development mode
        proxy_port = find_free_port(8080, 8090) or 8082
        web_port = find_free_port(8081, 8091) or 8083
        web_host = "127.0.0.1"
        
        local_ip = get_local_ip()
        
        print("=" * 60)
        print("MITM Proxy Web UI - Local Development")
        print("=" * 60)
        print()
        print(f"Proxy Server:   0.0.0.0:{proxy_port} (LAN accessible)")
        print(f"Web UI:         http://127.0.0.1:{web_port}")
        print()
        print("Configure your device:")
        print(f"  Proxy: {local_ip}:{proxy_port}")
        print()
        print("Press Ctrl+C to stop")
        print("=" * 60)
        print()
    
    # Run mitmweb
    cmd = [
        "mitmweb",
        "--mode", f"regular@0.0.0.0:{proxy_port}",
        "--web-host", web_host,
        "--web-port", str(web_port),
        "--no-web-open-browser",
        "--ssl-insecure"
    ]
    
    print(f"Starting mitmweb with command:")
    print(f"  {' '.join(cmd)}")
    print()
    sys.stdout.flush()
    
    try:
        # Run with output forwarded to stdout/stderr
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        print("ERROR: mitmweb not found!", file=sys.stderr)
        print("This should not happen in Docker. Check Dockerfile.", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"ERROR: mitmweb exited with code {e.returncode}", file=sys.stderr)
        sys.exit(e.returncode)
    except KeyboardInterrupt:
        print("\n\nStopped.")
        sys.exit(0)

if __name__ == "__main__":
    main()

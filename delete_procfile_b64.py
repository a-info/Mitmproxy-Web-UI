import urllib.request
import json
import ssl

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

TOKEN = "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"
REPO = "a-info/Mitmproxy-Web-UI"
FILENAME = "Procfile.b64"

def github_api(url, data=None, method=None):
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "mitm-proxy"
    }
    if data:
        headers["Content-Type"] = "application/json"
    
    req = urllib.request.Request(url, headers=headers, method=method)
    if data:
        req.data = json.dumps(data).encode()
    
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        try:
            error_body = e.read().decode()
            return e.code, json.loads(error_body) if error_body else {"error": str(e)}
        except:
            return e.code, {"error": str(e)}
    except Exception as e:
        return -1, {"error": str(e)}

print("="*60)
print("Deleting Procfile.b64 from GitHub")
print("="*60)

# Get file info to get SHA
print(f"\nStep 1: Getting file info...")
status, result = github_api(f"https://api.github.com/repos/{REPO}/contents/{FILENAME}")

if status == 200:
    sha = result.get("sha")
    print(f"  ✓ File found, SHA: {sha[:10]}...")
    
    # Delete the file
    print(f"\nStep 2: Deleting file...")
    data = {
        "message": "Remove Procfile.b64 - causing Railway deployment issues",
        "sha": sha,
        "branch": "main"
    }
    
    status, result = github_api(
        f"https://api.github.com/repos/{REPO}/contents/{FILENAME}",
        data=data,
        method="DELETE"
    )
    
    if status == 200:
        print(f"  ✓ SUCCESS! File deleted")
        print(f"  Commit: {result['commit']['sha'][:7]}")
        print("\n" + "="*60)
        print("Railway will now redeploy automatically!")
        print("="*60)
    else:
        print(f"  ✗ FAILED! Status: {status}")
        print(f"  Response: {result}")
        
elif status == 404:
    print(f"  ℹ File doesn't exist on GitHub (already deleted?)")
else:
    print(f"  ✗ Error: {status} - {result}")

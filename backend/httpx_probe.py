import os
import httpx

BASE = os.getenv("VLLM_BASE_URL", "http://192.168.130.24:8000/v1")

def print_env_proxies():
    for k in ["HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "http_proxy", "https_proxy", "all_proxy"]:
        if os.getenv(k):
            print(f"{k}={os.getenv(k)}")

print(f"BASE: {BASE}")
print("Env proxies (if any):")
print_env_proxies()

print("\n=== httpx default client ===")
try:
    r = httpx.get(f"{BASE}/models", timeout=10)
    print(r.status_code, r.text[:500])
except Exception as e:
    print("default client failed:", repr(e))

print("\n=== httpx no-proxy client ===")
try:
    with httpx.Client(proxies=None, timeout=10) as client:
        r = client.get(f"{BASE}/models")
        print(r.status_code, r.text[:500])
except Exception as e:
    print("no-proxy client failed:", repr(e))


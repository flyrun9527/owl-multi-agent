import json
import os
import sys
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

BASE = os.getenv("VLLM_BASE_URL_RAW", "http://192.168.130.24:8000")
AUTH = os.getenv("VLLM_API_KEY", "EMPTY")
MODEL = os.getenv("VLLM_MODEL_ID", "qwen3")

def fetch(url: str, method: str = "GET", data: dict | None = None):
    try:
        headers = {"Authorization": f"Bearer {AUTH}", "Content-Type": "application/json"}
        body = None
        if data is not None:
            body = json.dumps(data).encode("utf-8")
        req = Request(url=url, headers=headers, method=method, data=body)
        with urlopen(req, timeout=20) as resp:
            status = resp.status
            raw = resp.read()
            text = raw.decode("utf-8", errors="replace")
            print(f"\n[{method}] {url} -> {status}")
            print(text[:1000])
    except HTTPError as e:
        try:
            body = e.read().decode("utf-8", errors="replace")
        except Exception:
            body = "<no body>"
        print(f"\n[{method}] {url} -> HTTPError {e.code}\n{body[:1000]}")
    except URLError as e:
        print(f"\n[{method}] {url} -> URLError {e.reason}")
    except Exception as e:
        print(f"\n[{method}] {url} -> Exception {repr(e)}")

def main():
    print(f"BASE: {BASE}")
    # 探测常见端点
    fetch(f"{BASE}/v1/models")
    fetch(f"{BASE}/models")
    fetch(f"{BASE}")

    # 最小非流式聊天
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "说一句你好。"},
        ],
        "temperature": 0.0,
        "max_tokens": 64,
        "stream": False,
    }
    fetch(f"{BASE}/v1/chat/completions", method="POST", data=payload)

if __name__ == "__main__":
    main()


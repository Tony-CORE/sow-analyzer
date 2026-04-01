import requests

res = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "mistral",
        "prompt": "Say hello",
        "stream": False
    }
)

print(res.json()["response"])
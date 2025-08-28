import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

modelo = "mistralai/Mixtral-8x7B-Instruct-v0.1"
url = f"https://api-inference.huggingface.co/models/{modelo}"

headers = {
    "Authorization": f"Bearer {token}"
}

payload = {
    "inputs": "Hello, what is your name?"
}

response = requests.post(url, headers=headers, json=payload)

print(response.status_code)
print(response.json())

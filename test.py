import requests

url = "http://127.0.0.1:8000/sentiment"

data = {"text": "This restaurant is awesome"}

response = requests.post(url, json=data)

print(response.json())
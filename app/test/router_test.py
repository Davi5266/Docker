import requests

url = "http://localhost:8000/token"

data = {
    "username": "seu_usuario",
    "password": "sua_senha"
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(url, data=data, headers=headers)

print(response.status_code)
print(response.json())

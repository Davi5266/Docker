import requests

# url = "http://localhost:8000/token"
url = "http://192.168.0.113:8000/client/register"

# data = {
#     "username": "seu_usuario",
#     "password": "sua_senha"
# }

data = {
    "name": "me",
    "hashed_password": "me"
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

#response = requests.post(url=url, data=data, headers=headers)
response = requests.post("http://192.168.0.113:8000/client/register", data=data)

print(response.status_code)
print(response.json())

requests.post()

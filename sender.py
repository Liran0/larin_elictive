import requests
import time


host = 'http://127.0.0.1:5000'
url = '/send_messages'
login_url = '/login'
username = input("введии своё имя ")
password = input("введи пароль ")
response = requests.post(
    host+login_url,
    json = {"username": username, "password": password}
)

while not response.json()["ok"]:
    print("неверный логин или пороль")
    print()
    username = input("введии своё имя ")
    password = input("введи пароль ")
    requests.post(
        host+login_url,
        json = {"username": username, "password": password}
    )
print("доступ разрешён")
while True:
    text = input("введи текст сообщения ")
    requests.post(
        host+url,
        json = {"username": username, "text": text}
    )
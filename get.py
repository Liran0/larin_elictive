import requests

def print_message(message):
    print("Отпрвитель:", message["username"])
    print(message["text"])
    print(message["timestamp"])

host = 'http://127.0.0.1:5000'
url = '/get_messages'
after = 0


while True:
    response = requests.get(host+url)
    messages = response.json()["messages"]
    for message in messages:
        if after < message["timestamp"]:
            print_message(message)
    after = message["timestamp"]

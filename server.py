from flask import Flask, request
from time import time

app = Flask(__name__)
server_start_time = time()

messages = [
    {'username': 'ваня Бо', 'text': ' привет ', "timestamp": time()},
    {'username': 'тёма', 'text': ' и тебе привет ', "timestamp": time()},
    {'username': 'антон', 'text': ' да ', "timestamp": time()}

]
users = [
    {'username': 'ваня Бо', 'password': 'бо'},
    {'username': 'тёма', 'password': 'да'},
    {'username': 'Liran', 'password': 'Liran'},
]


@app.route('/get_messages')
def get_messages():
    return {
        'messages': messages

    }


@app.route('/send_messages', methods={'GET', 'POST'})
def send_messages():
    username = request.json["username"]
    text = request.json["text"]
    messages.append(
        {
            "username": username,
            "text": text,
            "timestamp": time()
        }
    )
    return (
        {"ok": True}

    )


@app.route('/')
def hallo():
    return 'ваня  0 импакта <a href = "/get_messages">get_messages</a>' \
           '<a href = "/status">его статус</a>'


@app.route('/status')
def status():
    return {
        'status': 'OK',
        'name': 'massager by Larin',
        'time': time()

    }


@app.route('/login', methods={'POST'})
def login():
    username = request.json["username"]
    password = request.json["password"]
    login_ok = False
    for user in users:
        if user['username'] == username:
            if user['password'] == password:

                login_ok = True
                break


if __name__ == '__main__':
    app.run(debug=True)

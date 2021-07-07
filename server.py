import time
from datetime import datetime

from flask import Flask, request, abort

app = Flask(__name__)
db = [
    {
        'text': 'Hello!',
        'name': 'Jack',
        'time': time.time()
    },
    {
        'text': 'Hello, Jack!',
        'name': 'John',
        'time': time.time()
    }
]

@app.route("/")
def hello():
    return "Hello, World! <a href='/status'>Status</a>"

@app.route("/status")
def status():
    now = datetime.now()
    return {
        'status': True,
        'name': 'Messenger in Python',
        'time0': time.time(),
        'time1': time.asctime(),
        'time2': now,        #dangerous
        'time3': str(now),
        'time4': now.isoformat(),
        'time5': now.strftime('%H:%M:%S')
    }

@app.route("/send", methods=['POST'])
def send_message():
    data = request.json

    # Check data is dict with text & name.
    if not isinstance(data, dict):
        return abort(400)
    if 'text' not in data or 'name' not in data:
        return abort(400)

    text = data['text']
    name = data['name']

    # Check text & name are valid strings.
    if not isinstance(text, str) or not isinstance(name, str):
        return abort(400)
    if len(text) == 0 or len(name) == 0:
        return abort(400)
    if len(text) > 1000 or len(name) > 100:
        return abort(400)

    message = {
        'text': text,
        'name': name,
        'time': time.time()
    }
    db.append(message)

    return {'ok': True}


@app.route("/messages")
def get_messages():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    result = []

    for message in db:
        if message['time'] > after:
            result.append(message)

    return {'messages': result[:100]}


app.run() # Запуск сервера.

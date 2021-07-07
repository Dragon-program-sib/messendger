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
    return "OK"

app.run() # Запуск сервера.

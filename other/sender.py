import requests

name = input('Введите имя: ')

while True:
    text = input('Введите сообщение: ')
    requests.post(
        'http://127.0.0.1:5000/send',
        json={'text': text, 'name': name}
    )
    
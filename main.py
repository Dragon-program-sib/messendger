import time
from datetime import datetime

# 1) Database
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

# 2) send_message

def send_message(text, name):
    message = {
        'text': text,
        'name': name,
        'time': time.time()
    }
    db.append(message)


# 3) get_messages

def get_messages(after):
    result = []

    for message in db:
        if message['time'] > after:
            result.append(message)

    return result


# messages = get_messages(0)

def print_messages(messages):
    for message in messages:
        print(datetime.fromtimestamp(message['time']), message['name'])  # datetime.fromtimestamp() - Высчитывает на стороне клиента, время согласно его часового пояса.
        print(message['text'])
        print()
    print('-' * 50)


print_messages(db)
send_message('Привет!', 'Борис')
send_message('Привет, Борис!', 'Иван')
print_messages(db)

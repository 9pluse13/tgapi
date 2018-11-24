import requests
url = 'https://api.telegram.org/bot686350094:AAHtSXznSXOZjpfYiGj4Vg7aoBB_EX7Hnyw/sendmessage'
params = {'chat_id': '@TruPC', 'text': 'test'}
r = requests.get(url, params=params)
print(r)

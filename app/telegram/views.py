import time
import requests
from flask import render_template

# from app.telegram import telega
# from . import telega

BOT_TOKEN = '5224798347:AAGzMX8bv2ghwYjGw1Wq2jIXtvtm-XMwCTU'
API_LINK = f'https://api.telegram.org/bot{BOT_TOKEN}'


def get_updates():
    old_id = 0
    new_id = 0
    while True:
        try:
            updates = requests.get(API_LINK + '/getUpdates?offset=-1').json()
            # updates = requests.get(API_LINK + '/getUpdates?offset=-1').json()
            message = updates['result'][0]['message']
            update_id = updates['result'][0]['update_id']
            new_id = update_id
            chat_id = message['from']['id']

            if message['text'] == '/start' and old_id != new_id:
                send_message = requests.get(API_LINK + f'/sendMessage?chat_id={chat_id}&text=Enter command /getcode for new pass')
                old_id = new_id

            elif message['text'] == '/getcode' and old_id != new_id:
                # print(old_id)
                send_message = requests.get(API_LINK + f'/sendMessage?chat_id={chat_id}&text=1234567890')
                old_id = new_id
                print('tyt 3', old_id)

            else:
                print('tyt 4')
                time.sleep(5)
        except KeyError:
            continue



# @telega.route('/login', methods=['GET', 'POST'])
# def login():
#     return render_template('telegram/login_telegram.html')


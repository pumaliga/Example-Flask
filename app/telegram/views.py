import time
import requests
from flask import render_template
# from . import telega

BOT_TOKEN = '5224798347:AAGzMX8bv2ghwYjGw1Wq2jIXtvtm-XMwCTU'
API_LINK = f'https://api.telegram.org/bot{BOT_TOKEN}'


# def get_updates():
#     while True:
#         updates = requests.get(API_LINK + '/getUpdates').json()
#         message = updates['result'][0]['message']
#         chat_id = message['from']['id']
#         text = message['text']
#         if text == '/getcode':
#             send_message = requests.get(API_LINK + f'/sendMessage?chat_id={chat_id}&text=1234567890')
#
#         else:
#             time.sleep(4)

        #     print('hahaha')
        # send_message = requests.get(API_LINK + f'/sendMessage?chat_id={chat_id}&text=1234567890')
        # time.sleep(4)

        # message = updates['result'][0]['message']
        # chat_id = message['from']['id']
        # text = message['text']
        # send_message = requests.get(API_LINK + f'/sendMessage?chat_id={chat_id}&text=Fuck you')

        # time.sleep(5)

# print(get_updates())


# @telega.route('/login', methods=['GET', 'POST'])
# def login():
#     return render_template('telegram/login_telegram.html')


import random
import string
import time

import requests
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user

from app.models import session, User
from app.register import Registration, User, new_user

views = Blueprint("views", __name__)
BOT_TOKEN = '5224798347:AAGzMX8bv2ghwYjGw1Wq2jIXtvtm-XMwCTU'
chanel_id = -1001226521608


def my_token(n):
    """ Function to generate a new password for telegram bot """
    token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(n))
    current_datetime = int(time.time())
    return token, current_datetime


def validator(user_id):
    method= "getChatMember"
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/{method}'
    data = {'chat_id': chanel_id, 'user_id': user_id}
    result = requests.post(url, data=data)
    return result.json()


def send_message(chat_id, text, username):
    method = "sendMessage"
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/{method}'
    data = {'chat_id': chat_id, "text": text}
    requests.post(url, data=data)
    if new_user.exist_user(username):
        new_user.create(username=username, password=text[0], time_register=text[1])
    else:
        new_user.update_time(username=username, password=text[0], time_register=text[1])

    # with session() as s:
    #     user = s.query(User).filter_by(username=username).first()
    #     if not user:
    #         new_user = User(username=username, password=text[0], create_pass=text[1])
    #         s.add(new_user)
    #     else:
    #         user.password = text[0]
    #         user.create_pass = text[1]
    #     s.commit()


@views.route('/', methods=["GET", "POST"]) # http://192.168.1.69:5000/ telegram sends messages to this address
def index():
    if request.method == "POST":
        try:
            print(request.json)
            message = request.json['message']['text']
            chat_id = request.json['message']['chat']['id']
            username = request.json['message']['from']['username']
            user_id = request.json['message']['from']['id']
            # if enter this command, bot send message this user with new password
            if message == '/getcode':
                # This func checks if the user is in a group
                member = validator(user_id)
                status = member['result']['status']
                if status in ('member', 'creator', 'administrator'):
                    send_message(chat_id, text=my_token(8), username=username)
            return {"Ok": True}
        except KeyError as e:
            print(e)
    return render_template('welcome.html')


@views.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username') # your username from telegram
    password = request.form.get('password') # password from telegram bot

    # if request.method == "POST":
    #     if username and password:
    #         with session() as s:
    #             user = s.query(User).filter_by(username=username).first()
    #             time_create = user.create_pass
    #             time_now = int(time.time())
    #             time_range = time_now - time_create
    #             if user.password == password and time_range < 15:
    #                 login_user(user)
    #                 return redirect(url_for('main.index'))
    #
    #     flash('Invalid username or password.')

    return render_template('login.html')


@views.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('views.login'))


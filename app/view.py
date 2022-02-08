import random
import string

import requests
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user

from app.models import session, User

views = Blueprint("views", __name__)
BOT_TOKEN = '5224798347:AAGzMX8bv2ghwYjGw1Wq2jIXtvtm-XMwCTU'


def my_token(n):
    """ Function to generate a new password for telegram bot """
    token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(n))
    return token


def send_message(chat_id, text, username):
    method = "sendMessage"
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/{method}'
    data = {'chat_id': chat_id, "text": text}
    requests.post(url, data=data)
    with session() as s:
        # get user from db, if user exist, replace old pass with new pass
        # else create new user with new password and username, where field username this your username from telegram
        user = s.query(User).filter_by(username=username).first()
        if not user:
            new_user = User(username=username, password=text)
            s.add(new_user)
        else:
            user.password = text
        s.commit()


@views.route('/', methods=["GET", "POST"]) # http://192.168.1.69:5000/ telegram sends messages to this address
def index():
    if request.method == "POST":
        chat_id = request.json['message']['chat']['id']
        message = request.json['message']['text']
        username = request.json['message']['from']['username']
        if message == '/getcode':
            # if enter this command, bot send message this user with new password
            send_message(chat_id, text=my_token(8), username=username)
        return {"Ok": True}

    return render_template('welcome.html')


@views.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username') # your username from telegram
    password = request.form.get('password') # password from telegram bot

    if request.method == "POST":
        if username and password:
            with session() as s:
                user = s.query(User).filter_by(username=username).first()
                if user.password == password:
                    login_user(user)
                    return redirect(url_for('main.index'))

        flash('Invalid username or password.')

    return render_template('login.html')


@views.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('views.login'))


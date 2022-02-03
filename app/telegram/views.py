from flask import render_template
from . import telega


@telega.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('telegram/login_telegram.html')


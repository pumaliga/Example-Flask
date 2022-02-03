from flask import request, redirect, flash, render_template, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from . import auth
from ..models import session, User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        with session() as s:
            user = s.query(User).filter_by(username=username).first()

            if check_password_hash(user.password, password):
                login_user(user)
                next_page = request.args.get('next')
                if next_page is None or not next_page.startswith('/'):
                    next_page = url_for('main.index')
                return redirect(next_page)
    flash('Invalid username or password.')

    return render_template('auth/login_telegram.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    if request.method == "POST":
        if username and password:
            with session() as s:
                hash_pass = generate_password_hash(password)
                new_user = User(username=username, password=hash_pass)
                s.add(new_user)
                s.commit()
        else:
            flash('Please, fill all fields! ')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))



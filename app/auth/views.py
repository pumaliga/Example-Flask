from flask import request, redirect, flash, render_template, url_for
from flask_login import login_user

from . import auth
from ..models import session, User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        with session() as s:
            user = s.query(User).filter_by(username=username).first()

            login_user(user)
            next_page = request.args.get('next')
            redirect(next_page)
    else:
        flash('Username or password is not correct!')

    return render_template('auth/login.html')



@auth.route('/register', methods=['GET', 'POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    if request.method == "POST":
        if username and password:
            with session() as s:
                # hash_pass = generate_password_hash(password)
                new_user = User(username=username, password=password)
                s.add(new_user)
                s.commit()
        else:
            flash('Please, fill all fields! ')
        return redirect(url_for('admin.login'))

    return render_template('register.html')

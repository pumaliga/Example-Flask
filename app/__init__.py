from flask import Flask, redirect, url_for
from flask_login import LoginManager


login_manager = LoginManager()

login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key'
    app.debug = True
    login_manager.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/main')

    @app.route('/')
    def redirect_rout():
        return redirect(url_for('auth.login'))

    return app



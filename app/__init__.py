from flask import Flask
from flask_login import LoginManager


login_manager = LoginManager()
# login_manager.login_view = 'auth.login'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = 'app/uploads'

def create_app():
    app = Flask(__name__)
    login_manager.init_app(app)
    app.config['SECRET_KEY'] = 'secret-key'
    app.debug = True


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/main')

    from app.view import views
    app.register_blueprint(views)

    return app



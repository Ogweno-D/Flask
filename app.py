from flask import Flask
from extensions import db
from flask_login import LoginManager


def create_app():
    
    app = Flask(__name__)
    
    app.config.from_prefixed_env()
    
    db.init_app(app)
    
    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(str(user_id))
    
    return app
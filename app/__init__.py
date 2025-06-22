from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# to interact with database throught app, we will use db
db = SQLAlchemy()

# keeping track of who logged in
login_manager = LoginManager()

# telling flask where to redirect unauthenticated users
login_manager.login_view = 'auth.login'

# Flash message category for when login is required
login_manager.login_message_category = 'info'


# Flask login user loader
@login_manager.user_loader
def load_user(user_id):
    from . import models
    return db.session.get(models.User, int(user_id))


# create Flask app instance
def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # SECRET_KEY and DATABASE_URL
    app.config.from_pyfile('config.py')

    # initialize extentions with Flask app
    db.init_app(app)
    login_manager.init_app(app)

    # Prefixes (using Blueprint)
    # Auth Blueprint
    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Main Blueprint
    from .routes.main import main_bp
    app.register_blueprint(main_bp)

    # Snippets Blueprint
    from .routes.snippets import snippets_bp
    app.register_blueprint(snippets_bp, url_prefix='/snippets')

    from . import models
    # Necessary for db operations, operates withing Flask's context
    with app.app_context():
        db.create_all()

    return app

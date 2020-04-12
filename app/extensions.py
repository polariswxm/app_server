from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_moment import Moment

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
moment = Moment()


def config_extentions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)

    # session protect level
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'user.login'
    login_manager.login_message = 'You need to login firstly'

from flask import Flask, render_template
from app.config import config
from app.extensions import config_extentions
from app.views import config_blueprint

# app = Flask(__name__)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    config_extentions(app)
    config_blueprint(app)

    config_errorhandler(app)
    return app


def config_errorhandler(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html')
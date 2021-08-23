from flask import Flask
from config import DevelopmentConfig
from tny.main.routes import main
from tny.api.routes import api

def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    # register blueprints
    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix="/api")
    return app

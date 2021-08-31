from flask import Flask
from tny.utils.redis import RedisClient
from tny.main import create_main_blueprint
from tny.api import create_api_blueprint

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    redis = RedisClient(config)
    # register blueprints
    main = create_main_blueprint(config, redis)
    api = create_api_blueprint(config, redis)
    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix="/api")
    return app

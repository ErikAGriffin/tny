from flask import Blueprint
from . import routes

def create_api_blueprint(config, db):
    api = Blueprint('api', __name__)

    routes.urls(api, config, db)

    return api

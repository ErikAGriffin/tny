from os import environ
from dotenv import load_dotenv

load_dotenv()

class BaseConfig(object):
    SHARED_KEY_EXAMPLE = True

class DevelopmentConfig(BaseConfig):
    REDIS_HOST = environ.get('REDIS_HOST') or "localhost"
    REDIS_PORT = environ.get('REDIS_PORT') or 6379
    TNY_HOSTNAME = "localhost:5000"

class ProductionConfig(BaseConfig):
    REDIS_HOST = environ.get('REDIS_HOST')
    REDIS_PORT = environ.get('REDIS_PORT')
    TNY_HOSTNAME = environ.get('TNY_HOSTNAME')

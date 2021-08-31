from tny import create_app
from config import DevelopmentConfig, ProductionConfig
from os import environ

if environ.get('TNY_ENV') == 'production':
    config = ProductionConfig
else:
    config = DevelopmentConfig

app = create_app(config)

if __name__ == '__main__':
    app.run()

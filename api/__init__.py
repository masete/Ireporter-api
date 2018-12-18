from flask import Flask
from api.config import config
from api.routes import Routes


class Server:

    @staticmethod
    def create_app(config = None):
        app = Flask(__name__)
        Routes.generate(app)
        return app


APP = Server().create_app(config=config.DevelopmentConfig)

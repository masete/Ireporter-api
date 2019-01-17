"""
module Starting my flask instance
"""
from flask import Flask
from api.config import config
from api.config.routes import Routes


# class Server:
#     """
#     class containing the method to start the server
#     """

#     @staticmethod
#     def create_app(config=None):
#         """methods to start the app instance"""
#         app = Flask(__name__)
#         Routes.generate(app)
#         return app
#
#
# APP = Server().create_app(config=config.DevelopmentConfig)

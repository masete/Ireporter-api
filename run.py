"""
Main app root of the api endpoints
"""
from flask import Flask
from api.config import config
from api.config.routes import Routes


class Server:
    """
    Create loader object to start server
    """

    def __init__(self):
        """
        my init method, where am creating an instance of class Routes
        """
        self.route = Routes()

    def create_app(self, env_name):
        """
        static method for starting a server
        """
        # app initiliazation
        app = Flask(__name__)
        app.config.from_object(config.APP_CONFIG[env_name])

        # Directing to Routes
        self.route.generate(app)

        return app


app = Server().create_app('development')

if __name__ == '__main__':
    app.run(port=2000)

"""
Routes module to handle request urls
"""
from flask import request
from api.views.redflag_views import RedFlagViews
from api.views.user_view import UserView


class Routes:
    flag_views = RedFlagViews()
    user_views = UserView()
    """
    Class to generate urls
    """
    def generate(self, app):

        @app.route('/api/v1/red-flags/', methods=['POST', 'GET'], strict_slashes=False)
        def red_flags():
            if request.method == 'POST':
                return self.flag_views.create_flag()
            return self.flag_views.get_flag()

        @app.route('/api/v1/red-flags/<int:red_flag_id>', methods=['GET'], strict_slashes=False)
        def get_single_flag(red_flag_id):
            return self.flag_views.get_flag(red_flag_id)

        @app.route('/api/v1/red-flags/<int:red_flag_id>', methods=['DELETE'], strict_slashes=False)
        def delete_flag(red_flag_id):
            return self.flag_views.delete_flag(red_flag_id)

        @app.route('/api/v1/red-flags/<int:red_flag_id>', methods=['PUT'], strict_slashes=False)
        def edit_flag(red_flag_id):
            return self.flag_views.edit_flag(red_flag_id)

        @app.route('/api/auth/user', methods=['POST'], strict_slashes=False)
        def signup_user():
            return self.user_views.signup()

        @app.route('/api/auth/login', methods=['POST'], strict_slashes=False)
        def login_user():
            return self.user_views.login()


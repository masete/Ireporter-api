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
        """
        my generate method to route my views
        :param app:
        :return:
        """

        @app.route('/api/v1/red-flags/', methods=['POST', 'GET'], strict_slashes=False)
        def red_flags():
            """
            method routing us to POST and Get methods views for redflags
            :return:
            """
            if request.method == 'POST':
                return self.flag_views.create_flag()
            return self.flag_views.get_flag()

        @app.route('/api/v1/red-flags/<int:flag_id>', methods=['GET'], strict_slashes=False)
        def get_single_flag(flag_id):
            """
            method routing us to my methods for getting a single redflag
            :param flag_id:
            :return:
            """
            return self.flag_views.get_flag(flag_id)

        @app.route('/api/v1/red-flags/<int:flag_id>', methods=['DELETE'], strict_slashes=False)
        def delete_flag(flag_id):
            """
            method for deleting a redflag
            :param flag_id:
            :return:
            """
            return self.flag_views.delete_flag(flag_id)

        @app.route('/api/v1/red-flags/<int:flag_id>', methods=['PUT'], strict_slashes=False)
        def edit_flag(flag_id):
            """
            method routing us to view editing a redflag
            :param flag_id:
            :return:
            """
            return self.flag_views.edit_flag(flag_id)

        @app.route('/api/auth/user', methods=['POST'], strict_slashes=False)
        def signup_user():
            """
            method routing us to creating user view
            :return:
            """
            return self.user_views.signup()

        @app.route('/api/auth/login', methods=['POST'], strict_slashes=False)
        def login_user():
            """
            method for routing to view to login user
            :return:
            """
            return self.user_views.login()

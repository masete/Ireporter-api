"""
Routes module to handle request urls
"""
from flask import request
from api.views.redflag_views import RedFlagViews
from api.views.user_view import UserView


class Routes:
    flag_views = RedFlagViews()
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
        def get_single_parcel(red_flag_id):
            return self.flag_views.get_flag(red_flag_id)

        # app.add_url_rule('/api/v1/redflags/', view_func=RedFlagViews.as_view('create_redflag'),
        #                  methods=['POST'], strict_slashes=False)

        # app.add_url_rule('/api/v1/redflags/', view_func=RedFlagViews.as_view('get_all_redflags'),
        #                  methods=['GET'], strict_slashes=False)

        app.add_url_rule('/api/v1/redflags/<int:red_flag_id>', view_func=RedFlagViews.as_view('get_all_specific_redflag'),
                         methods=['GET'], strict_slashes=False)

        app.add_url_rule('/api/v1/redflags/<int:red_flag_id>',
                         view_func=RedFlagViews.as_view('edit_redflag'),
                         methods=['PUT'], strict_slashes=False)

        app.add_url_rule('/api/v1/redflags/<int:red_flag_id>',
                         view_func=RedFlagViews.as_view('delete_redflag'),
                         methods=['DELETE'], strict_slashes=False)

        app.add_url_rule('/api/auth/user/',
                         view_func=UserView.as_view('create'),
                         methods=['POST'], strict_slashes=False)

        app.add_url_rule('/api/login/user/',
                         view_func=UserView.as_view('login_user'),
                         methods=['POST'], strict_slashes=False)





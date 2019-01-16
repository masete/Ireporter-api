"""
Routes module to handle request urls
"""
from api.views.redflag_views import RedflagViews
from api.views.user_view import UserView


class Routes:
    """
    Class to generate urls
    """
    @staticmethod
    def generate(app):

        app.add_url_rule('/api/v1/redflags/', view_func=RedflagViews.as_view('create_redflag'),
                         methods=['POST'], strict_slashes=False)

        app.add_url_rule('/api/v1/redflags/', view_func=RedflagViews.as_view('get_all_redflags'),
                         methods=['GET'], strict_slashes=False)

        app.add_url_rule('/api/v1/redflags/<int:red_flag_id>', view_func=RedflagViews.as_view('get_all_specific_redflag'),
                         methods=['GET'], strict_slashes=False)

        app.add_url_rule('/api/v1/redflags/<int:red_flag_id>',
                         view_func=RedflagViews.as_view('edit_redflag'),
                         methods=['PUT'], strict_slashes=False)

        app.add_url_rule('/api/v1/redflags/<int:red_flag_id>',
                         view_func=RedflagViews.as_view('delete_redflag'),
                         methods=['DELETE'], strict_slashes=False)

        app.add_url_rule('/api/auth/user/',
                         view_func=UserView.as_view('create_user'),
                         methods=['POST'], strict_slashes=False)



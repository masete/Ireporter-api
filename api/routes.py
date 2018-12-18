"""
Routes module to handle request urls
"""
from api.views.redflag_views import RedflagViews


class Routes:
    """
    Class to generate urls
    """
    @staticmethod
    def generate(app):
        """
        Generate urls on the app context
        :param app:
        :return:
        """
        app.add_url_rule('/api/v1/redflag/', view_func=RedflagViews.as_view('create_redflag'),
                         methods=['POST'], strict_slashes=False)

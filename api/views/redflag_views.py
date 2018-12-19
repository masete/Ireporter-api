from flask import request, jsonify
from flask.views import MethodView
from api.models.redflags import Redflags
from api.Helpers.error_feedback import ErrorFeedback

class RedflagViews(MethodView):
    red = Redflags()
    createdBy = None
    red_flag_title = None
    red_flag_comment = None

    def post(self):
        data = request.get_json()
        try:
            self.createdBy = data["createdBy"].strip()
            self.red_flag_title = data["red_flag_title"].strip()
            self.red_flag_comment = data["red_flag_comment"].strip()
        except AttributeError:
            return ErrorFeedback.invalid_data_format()
        if not self.createdBy or not self.red_flag_title or not self.red_flag_comment:
            return ErrorFeedback.empty_data_fields()

        redflag_response = self.red.create_redflag(self.createdBy, self.red_flag_title, self.red_flag_comment)
        response_object = {
            'status': '201',
            'message': 'Redflag has been created',
            'data': redflag_response.__dict__
        }
        return jsonify(response_object), 201








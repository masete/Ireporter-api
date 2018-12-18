from flask import request, jsonify
from flask.views import MethodView
from api.models.redflags import Redflags


class RedflagViews(MethodView):
    red = Redflags()
    created_by = None
    red_flag_title = None
    red_flag_comment = None

    def post(self):
        data = request.get_json()
        self.created_by = data["created_by"].strip()
        self.red_flag_title = data["red_flag_title"].strip()
        self.red_flag_comment = data["red_flag_comment"].strip()

        redflag_response = self.red.create_redflag(self.created_by, self.red_flag_title, self.red_flag_comment)
        response_object = {
            'status': 'Success',
            'message': 'Redflag has been created',
            'data': redflag_response.__dict__
        }
        return jsonify(response_object), 201








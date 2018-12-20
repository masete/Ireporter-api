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

    def get(self, red_flag_id=None):
        if not self.red.redflags:
            return ErrorFeedback.empty_data_storage()
        elif red_flag_id:
            return self.get_specific_redflag(red_flag_id)

        response_object = {
            'status': '200',
            'data': [redflag.__dict__ for redflag in self.red.get_all_redflags()]
        }
        return jsonify(response_object), 200

    def get_specific_redflag(self, red_flag_id):
        for redflag in self.red.get_all_redflags():
            if redflag.red_flag_id == red_flag_id:
                response_object = {
                    'status': '200',
                    'message': 'Order exists',
                    'data': redflag.__dict__
                }
                return jsonify(response_object), 200

        return ErrorFeedback.no_redflag()

    def delete(self, red_flag_id):
        for redflag in self.red.redflags:
            if redflag['red_flag_id'] == red_flag_id:
                self.red.redflags.remove(redflag)
                return redflag
            return jsonify({"message": "no redflag to delete"})

    def put(self, red_flag_id=None):
        data = request.get_json()

        key = 'red_flag_title'
        if key not in data:
            return ErrorFeedback.missing_key
        try:
            red_flag_title = data['red_flag_title'].strip()
        except AttributeError:
            return ErrorFeedback.invalid_data_format()
        if not red_flag_title:
            return ErrorFeedback.empty_data_fields()

        return jsonify({'redflag': self.red.update_order(red_flag_title)}), 200













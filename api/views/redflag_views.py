from flask import request, jsonify
from flask.views import MethodView
from api.models.redflags import Redflags
from api.Helpers.error_feedback import ErrorFeedback


class RedflagViews(MethodView):
    red = Redflags()
    created_by = None
    flag_title = None
    flag_location = None
    flag_comment = None
    flag_type = None

    def post(self):
        data = request.get_json()

        keys = ("created_by", "flag_title", "flag_location", "flag_comment")
        if not set(keys).issubset(set(request.json)):
            return ErrorFeedback.missing_key(keys)

        self.created_by = data["created_by"]
        self.flag_title = data["flag_title"]
        self.flag_location = data['flag_location']
        self.flag_comment = data['flag_comment']

        if not isinstance(request.json['flag_location'], int):
            return ErrorFeedback.invalid_data_type()

        if not isinstance(request.json['flag_title'], str):
            return ErrorFeedback.invalid_data_type_str()

        if not isinstance(request.json['flag_comment'], str):
            return ErrorFeedback.invalid_data_type_str()

        if not self.created_by or not self.flag_title or not self.flag_comment:
            return ErrorFeedback.empty_data_fields()

        for flag in self.red.redflags:
            if self.flag_comment in flag.flag_comment:
                return jsonify({"message": "record already exits please post a new redflag with "
                                           "completely different flag comment from the existing"}), 400

        flag_response = self.red.create_redflag(self.created_by, self.flag_title, self.flag_location,
                                                self.flag_comment)
        response_object = {
            'status': '201',
            'message': 'Redflag has been created',
            'data': flag_response.__dict__
        }
        return jsonify(response_object), 201

    def get(self, red_flag_id=None):
        if not self.red.redflags:
            return ErrorFeedback.empty_data_storage()
        elif red_flag_id:
            return self.get_specific_redflag(red_flag_id)

        response_object = {
            'status': '200',
            'data': [flag.__dict__ for flag in self.red.get_all_redflags()]
        }
        return jsonify(response_object), 200

    def get_specific_redflag(self, red_flag_id):
        for flag in self.red.get_all_redflags():
            if flag.red_flag_id == red_flag_id:
                response_object = {
                    'status': '200',
                    'message': 'red flag exists',
                    'data': flag.__dict__
                }
                return jsonify(response_object), 200

        return ErrorFeedback.no_redflag()

    def delete(self, red_flag_id):
        for redflag in self.red.redflags:
            if redflag.red_flag_id == red_flag_id:
                self.red.redflags.remove(redflag)
                return jsonify({"status": 200, "data": [{"id": red_flag_id, "message": "redflag record has been deleted"
                                                        }]}), 200
        return jsonify({"message": "no redflag to delete"}), 400

    def put(self, red_flag_id):
        data = request.get_json()

        if ('type' not in data) and ('payload' not in data):
            return ErrorFeedback.missing_key

        self.red_flag_type = data['payload']
        single_record = [record.__dict__ for record in self.red.redflags if record.__dict__['red_flag_id']
                         == red_flag_id]

        if not single_record:
            return jsonify({"message": "no record"}), 400
        single_record[0][data['type']] = data['payload']
        return jsonify({"status": "200", "data": [{"edited redflag": single_record, "message":
                       "red flag record has been edited"}]})








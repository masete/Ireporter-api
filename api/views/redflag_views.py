from flask import request, jsonify
from flask.views import MethodView
from api.models.redflags import RedFlags
from api.Helpers.error_feedback import ErrorFeedback


class RedFlagViews(MethodView):
    models = RedFlags()
    created_by = None
    flag_title = None
    flag_location = None
    flag_comment = None
    flag_type = None

    def create_flag(self):
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

        if self.flag_comment == self.models.redFlags:
            return jsonify({"message": "record already exits"})

        red_flag_response = self.models.create_red_flag(self.created_by, self.flag_title, self.flag_location,
                                                        self.flag_comment)
        response_object = {
            'status': '201',
            'message': 'Redflag has been created',
            'data': red_flag_response.__dict__
        }
        return jsonify(response_object), 201

    def get_flag(self, red_flag_id=None):
        if not self.models.redFlags:
            return ErrorFeedback.empty_data_storage()
        elif red_flag_id:
            return self.models.get_specific_red_flag(red_flag_id)

        flag_response = [flag.__dict__ for flag in self.models.get_all_red_flags()]

        response_object = {
            'status': '200',
            'data': flag_response
        }
        return jsonify(response_object), 200

    def delete_flag(self, red_flag_id):
        for flag in self.models.redFlags:
            if flag.red_flag_id == red_flag_id:
                self.models.redFlags.remove(flag)
                return jsonify({"status": 200, "data": [{"id": red_flag_id, "message": "redflag record has been deleted"
                                                        }]}), 200
        return jsonify({"message": "no redflag to delete"}), 400

    def edit_flag(self, red_flag_id):
        single_record = [record.__dict__ for record in self.models.redFlags if
                         record.red_flag_id == red_flag_id]
        if single_record:
            data = request.get_json()

            single_record[0]['created_by'] = data.get('created_by', single_record[0]['created_by'])
            single_record[0]['flag_title'] = data.get("flag_title", single_record[0]['flag_title'])
            single_record[0]['flag_location'] = data.get('flag_location', single_record[0]['flag_location'])
            single_record[0]['flag_comment'] = data.get('flag_comment', single_record[0]['flag_comment'])

            self.models.redFlags.append(single_record)
            return jsonify({"message": "edited", "data": single_record})










from api.models.const.redflag_model import RedflagModel
from flask import jsonify


class RedFlags:

    index = 0
    redFlags = []

    def create_red_flag(self, created_by, red_flag_title, red_flag_location, red_flag_comment):
        self.index += 1
        red_flag = RedflagModel(created_by, red_flag_title, red_flag_location, red_flag_comment)
        red_flag.red_flag_id = self.index
        self.redFlags.append(red_flag)

        return red_flag

    def get_all_red_flags(self):
        return self.redFlags

    def get_specific_red_flag(self, red_flag_id):
        for flag in self.redFlags:
            if red_flag_id == flag.red_flag_id:
                response_object = {
                    'status': '200',
                    'message': 'redflag exists',
                    'data': flag.__dict__
                            }
                return jsonify(response_object), 200
        return None











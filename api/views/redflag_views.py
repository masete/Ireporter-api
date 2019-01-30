"""
module containing my redflag views
"""
from flask import request, jsonify
from flask.views import MethodView
from api.models.redflags import RedFlags
from api.Helpers.error_feedback import ErrorFeedback
from api.Helpers.validators import validate_create_red_flag
import jwt
from functools import wraps


def token_req(end_point):
    """
    JWT method to get token from headers
    :param end_point:
    :return:
    """
    @wraps(end_point)
    def check(*args, **kwargs):
        if 'token' in request.headers:
            tk = request.headers['token']
        else:
            return jsonify({'message': 'you should login'})
        try:
            jwt.decode(tk, 'masete_nicholas_scretekey')
        except:
            return jsonify({'message': 'user not authenticated'})
        return end_point(*args, **kwargs)

    return check


class RedFlagViews(MethodView):
    """
    my class with instance variables
    """
    models = RedFlags()

    def create_flag(self):
        """
        method to create redflag
        :return:
        """
        data = request.get_json()

        keys = ("created_by", "flag_title", "flag_latitude", "flag_longitude", "flag_comment")
        if not set(keys).issubset(set(request.json)):
            return ErrorFeedback.missing_key(keys)

        created_by = data.get("created_by")
        flag_title = data.get("flag_title")
        flag_latitude = data.get('flag_latitude')
        flag_longitude = data.get('flag_longitude')
        flag_comment = data.get('flag_comment')

        red_flag_response = self.models.create_red_flag(created_by=created_by, flag_title=flag_title,
                                                        flag_latitude=flag_latitude,
                                                        flag_longitude=flag_longitude, flag_comment=flag_comment)

        val = validate_create_red_flag(created_by, flag_title, flag_comment)
        if val:
            return val

        response_object = {
            'status': '201',
            'message': 'Redflag has been created',
            'data': red_flag_response.to_json()
        }
        return jsonify(response_object), 201

    def get_flag(self, flag_id=None):
        """
        method to get all redflags and a specific redflag
        :param flag_id:
        :return:
        """
        if not self.models.redFlags:
            return ErrorFeedback.empty_data_storage()
        elif flag_id:
            return self.models.get_specific_red_flag(flag_id)

        flag_response = self.models.get_all_red_flags()

        response_object = {
            'status': '200',
            'data': flag_response
        }
        return jsonify(response_object), 200

    def delete_flag(self, flag_id):
        """
        method to delete a redflag
        :param flag_id:
        :return:
        """
        deleted = self.models.delete_red_flag(flag_id)
        return deleted

    def edit_flag(self, flag_id):
        """
        method to edit a redflag
        :param flag_id:
        :return:
        """
        single_record = [record for record in self.models.redFlags if
                         record['flag_id'] == flag_id]
        if single_record:
            data = request.get_json()

            single_record[0]['created_by'] = data.get('created_by', single_record[0]['created_by'])
            single_record[0]['flag_title'] = data.get('flag_title', single_record[0]['flag_title'])
            single_record[0]['flag_latitude'] = data.get('flag_latitude', single_record[0]['flag_latitude'])
            single_record[0]['flag_longitude'] = data.get('flag_longitude', single_record[0]['flag_longitude'])
            single_record[0]['flag_comment'] = data.get('flag_comment', single_record[0]['flag_comment'])

            self.models.redFlags.append(single_record[0])
            return jsonify({"message": "edited", "data": single_record})
        return jsonify({"message": "there is no redflag with that id"}), 400

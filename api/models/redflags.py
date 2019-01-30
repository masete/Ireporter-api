"""
my module containing my redflag models
"""
from flask import jsonify
from datetime import datetime


class RedFlags:
    def __init__(self, **kwargs):
        self.flag_id = kwargs.get("flag_id")
        self.created_by = kwargs.get("created_by")
        self.flag_title = kwargs.get("flag_title")
        self.flag_latitude = kwargs.get("flag_latitude")
        self.flag_longitude = kwargs.get("flag_longitude")
        self.flag_comment = kwargs.get("flag_comment")
        self.createdOn = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.red_flag_status = "yet to be resolved"

    def to_json(self):
        flag = {
            'flag_id': self.flag_id,
            'created_by': self.created_by,
            'flag_title': self.flag_title,
            'flag_latitude': self.flag_latitude,
            'flag_longitude': self.flag_longitude,
            'flag_comment': self.flag_comment,
            'createdOn': self.createdOn,
            'red_flag_status': self.red_flag_status
        }
        return flag

    index = 0
    redFlags = []

    def create_red_flag(self, created_by, flag_title, flag_latitude, flag_longitude, flag_comment):
        """
        method to create a redfalg
        :param created_by:
        :param flag_title:
        :param flag_latitude:
        :param flag_longitude:
        :param flag_comment:
        :return:
        """
        self.index += 1
        red_flag = RedFlags(created_by=created_by, flag_title=flag_title, flag_latitude=flag_latitude,
                            flag_longitude=flag_longitude, flag_comment=flag_comment)
        red_flag.flag_id = self.index
        self.redFlags.append(red_flag.__dict__)

        return red_flag

    def get_all_red_flags(self):
        """
        method to get all redflags
        :return:
        """
        return self.redFlags

    def get_specific_red_flag(self, flag_id):
        """
        method to get a specific redflag
        :param flag_id:
        :return:
        """
        for flag in self.redFlags:
            if flag_id == flag['flag_id']:
                response_object = {
                    'status': '200',
                    'message': 'redflag exists',
                    'data': flag}
                return jsonify(response_object), 200
        return jsonify({"status": "404", "message": "that redflag does not exist"}), 404

    def delete_red_flag(self, flag_id):

        for flag in self.redFlags:
            if flag['flag_id'] == flag_id:
                self.redFlags.remove(flag)
                return jsonify({"status": 200, "data": [{"id": flag_id, "message": "redflag record has been deleted"
                                                         }]}), 200
        return jsonify({"message": "no redflag to delete"}), 400


"""
my module containing my redflag models
"""
from flask import jsonify
from api.models.const.redflag_model import RedFlagModel


class RedFlags:
    """
    class having methods manuplating views
    """

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
        red_flag = RedFlagModel(created_by=created_by, flag_title=flag_title, flag_latitude=flag_latitude,
                                flag_longitude=flag_longitude, flag_comment=flag_comment)
        red_flag.flag_id = self.index
        self.redFlags.append(red_flag)

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
            if flag_id == flag.flag_id:
                response_object = {
                    'status': '200',
                    'message': 'redflag exists',
                    'data': flag.to_json()}
                return jsonify(response_object), 200
        return jsonify({"status": "404", "message": "that redflag does not exist"}), 404

from api.models.const.redflag_model import RedflagModel
from flask import jsonify


class Redflags:

    index = 0
    redflags = []

    def create_redflag(self, createdBy, red_flag_title, red_flag_comment):
        self.index += 1
        redflag = RedflagModel(createdBy, red_flag_title, red_flag_comment)
        redflag.red_flag_id = self.index
        self.redflags.append(redflag)

        return redflag

    @classmethod
    def get_all_redflags(cls):
        return cls.redflags

    @classmethod
    def get_specific_redflag(cls, red_flag_id):
        for redflag in cls.redflags:
            if red_flag_id == redflag.red_flag_id:
                return redflag
        return None

    @classmethod
    def update_record(cls, red_flag_id, red_flag_comment=None):
        single_record = [record for record in cls.redflags if record.red_flag_id == red_flag_id]









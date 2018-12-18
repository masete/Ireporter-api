from api.models.const.redflag_model import RedflagModel
from typing import List


class Redflags:

    index = 0
    redflags : List[RedflagModel] = []

    def create_redflag(self, created_by, red_flag_title, red_flag_comment):
        self.index += 1
        redflag = RedflagModel(created_by, red_flag_title, red_flag_comment)
        redflag.red_flag_id = self.index
        self.redflags.append(redflag)

        return redflag



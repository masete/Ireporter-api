from datetime import datetime
# from api.Helpers.utility import JSONSerializable


class RedflagModel:
    def __init__(self, createdBy=None, red_flag_title=None, red_flag_comment=None):
        self.red_flag_id = None
        self.createdBy = createdBy
        self.red_flag_title = red_flag_title
        self.red_flag_comment = red_flag_comment
        self.createdOn = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.red_flag_status = "yet to be resolved"


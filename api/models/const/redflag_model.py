from datetime import datetime
# from api.Helpers.utility import JSONSerializable


class RedflagModel:
    def __init__(self, created_by=None, red_flag_title=None, red_flag_comment=None):
        self.red_flag_id = None
        self.created_by = created_by
        self.red_flag_title = red_flag_title
        self.red_flag_comment = red_flag_comment
        self.red_flag_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.red_flag_status = "yet to be resolved"


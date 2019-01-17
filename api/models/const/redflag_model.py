from datetime import datetime
# from api.Helpers.utility import JSONSerializable


class RedflagModel:
    def __init__(self, created_by=None, flag_title=None, flag_location=None, flag_comment=None):
        self.red_flag_id = None
        self.created_by = created_by
        self.flag_title = flag_title
        self.flag_location = flag_location
        self.flag_comment = flag_comment
        self.createdOn = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.red_flag_status = "yet to be resolved"


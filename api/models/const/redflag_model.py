"""model defining my constructor"""
from datetime import datetime


class RedFlagModel:
    """
    my constructor using kwargs
    """
    def __init__(self, **kwargs):
        self.flag_id = kwargs.get("flag_id")
        self.created_by = kwargs.get("created_by")
        self.flag_title = kwargs.get("flag_title")
        self.flag_latitude = kwargs.get("flag_latitude")
        self.flag_longitude = kwargs.get("flag_longitude")
        self.flag_comment = kwargs.get("flag_comment")
        self.createdOn = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.red_flag_status = "yet to be resolved"


from datetime import datetime


class UserAuth:
    users = []

    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.other_names = kwargs.get("other_names")
        self.user_name = kwargs.get("user_name")
        self.email = kwargs.get("email")
        self.phone_number = kwargs.get("phone_number")
        self.registered_on = kwargs.get("registered_on")
        self.is_admin = kwargs.get("is_admin")


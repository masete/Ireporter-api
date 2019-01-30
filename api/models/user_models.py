"""
my module containing user models
"""
from flask import jsonify
from _datetime import datetime


class UserAuth:
    """
    my class containing my constructor
    """
    users = []

    def __init__(self, **kwargs):
        self.user_id = len(self.users) + 1
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.other_names = kwargs.get("other_names")
        self.user_name = kwargs.get("user_name")
        self.email = kwargs.get("email")
        self.phone_number = kwargs.get("phone_number")
        self.registered_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.is_admin = kwargs.get("is_admin")
        self.password = kwargs.get("password")

    def to_json1(self):
        user1 = {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'other_names': self.other_names,
            'user_name': self.user_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'registered_on': self.registered_on,
            'is_admin': self.is_admin,
            'password': self.password
        }
        return user1

    def check_user_credentials(self, email, password):
        """
        mythod to login user
        :param email:
        :param password:
        :return:
        """
        for user in self.users:
            if user['email'] == email:
                if user['password'] == password:
                    return True
        return jsonify({"message": "wrong password or username"})

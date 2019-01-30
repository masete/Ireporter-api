"""
My module for user authentication routes
"""
from flask import request, jsonify
from flask.views import MethodView
from api.models.user_models import UserAuth
from api.Helpers.validators import validate_user_details
from api.Helpers.jwt_auth import encode_token


AUTH = UserAuth()


class UserView(MethodView):
    """
    my login and signup methods
    """
    def signup(self):

        data = request.get_json()

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        other_name = data.get("other_name")
        user_name = data.get("user_name")
        email = data.get("email")
        phone_number = data.get("phone_number")
        is_admin = data.get("is_admin")
        password = data.get("password")

        val = validate_user_details(first_name, last_name, other_name, user_name, email, phone_number, password,
                                    is_admin)
        if val:
            return val

        user = UserAuth(first_name=first_name, last_name=last_name, other_names=other_name, user_name=user_name,
                        email=email, phone_number=phone_number, is_admin=is_admin, password=password)
        UserAuth.users.append(user.to_json1())
        return jsonify({"massage": "user created successfully", "data": user.to_json1()}), 201

    def login(self):
        """
        my login method
        :return:
        """
        data = request.get_json()
        if isinstance(AUTH.check_user_credentials(data['email'], data['password']), bool):
            return jsonify({"status": 200, "data": [{"token": encode_token(data['email']),
                                                     "message": "Logged in successfully"}]}), 200
        return jsonify({"message": "wrong password or email"})

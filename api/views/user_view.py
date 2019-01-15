from flask import request, jsonify
from flask.views import MethodView
from api.models.user_models import UserAuth
from api.Helpers.validators import validate_user_details, validate_space


class UserView(MethodView):

    def post(self):

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
        space = validate_space(first_name, last_name, other_name, user_name, email, phone_number, password,
                               is_admin)
        if space:
            return space

        user = UserAuth(first_name=first_name, last_name=last_name, other_names=other_name, user_name=user_name,
                        email=email, phone_number=phone_number, is_admin=is_admin, password=password)
        UserAuth.users.append(user)
        return jsonify({"massage": "user created successfully"}), 201

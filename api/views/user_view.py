from flask import request, jsonify
from flask.views import MethodView
from api.models.user_models import UserAuth


class UserView(MethodView):

    def post(self):

        data = request.get_json()

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        other_names = data.get("other_names")
        user_name = data.get("user_name")
        email = data.get("email")
        phone_number = data.get("phone_number")
        is_admin = data.get("is_admin")

        user = UserAuth(first_name=first_name, last_name=last_name, other_names=other_names, user_name=user_name,
                        email=email, phone_number=phone_number, is_admin=is_admin)
        UserAuth.users.append(user)

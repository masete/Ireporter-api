from flask import jsonify
from validate_email import validate_email


def validate_user_details(first_name, last_name, other_name, user_name, email, phone_number, password, is_admin):
    if not first_name and last_name and other_name and user_name and email and phone_number and password and is_admin:
        return jsonify({"message": "all fields are required"}), 400

    if not first_name == "" and last_name == "" and other_name == "" and user_name == "" and email == "" \
            and phone_number == "" and password == "" and is_admin:
        return jsonify({"message": "fields cant be  empty"}), 400

    if not first_name == " " and last_name == " " and other_name == " " and user_name == " " and email == " " \
            and phone_number == " " and password == " " and is_admin:
        return jsonify({"message": "fields cant be passed empty strings"}), 400

    valid_email = validate_email(email)
    if not valid_email:
        return jsonify({
            "error": "Please use a valid email address for example nich@gmail"
        }), 400





from flask import request, jsonify
from validate_email import validate_email
from . error_feedback import ErrorFeedback
from api.models.redflags import RedFlags

models = RedFlags()


def validate_user_details(first_name, last_name, other_name, user_name, email, phone_number, password, is_admin):
    if not first_name and last_name and other_name and user_name and email and phone_number and password and is_admin:
        return jsonify({"message": "all fields are required"}), 400

    if not first_name == "" and last_name == "" and other_name == "" and user_name == "" and email == "" \
            and phone_number == "" and password == "" and is_admin:
        return jsonify({"message": "fields cant be  empty"}), 400

    valid_email = validate_email(email)
    if not valid_email:
        return jsonify({
            "error": "Please use a valid email address for example nich@gmail"
        }), 400

    if not first_name.isalpha() or not last_name.isalpha():
        return jsonify({
            "error": "First and last name should only be alphabets"
        }), 400


def validate_create_red_flag(created_by, flag_title, flag_comment):
    # for flag in models.redFlags:
    #     if flag['flag_comment'] == flag_comment:
    #         return jsonify({"message": "record already exits"})
    #     return None

    if not (isinstance(request.json['flag_latitude'], float) and isinstance(request.json['flag_longitude'], float)):
        return ErrorFeedback.invalid_data_type()

    if not isinstance(request.json['flag_title'], str):
        return ErrorFeedback.invalid_data_type_str()

    if not isinstance(request.json['flag_comment'], str):
        return ErrorFeedback.invalid_data_type_str()

    if not created_by or not flag_title or not flag_comment:
        return ErrorFeedback.empty_data_fields()











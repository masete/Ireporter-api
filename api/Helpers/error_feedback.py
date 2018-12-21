"""
Module to handle all error responses
"""
from flask import jsonify


class ErrorFeedback:
    """
    Error handler to handle response errors.
    """
    @staticmethod
    def invalid_data_format():
        response_object = {
            'status': '400',
            'error_message': 'Please use character strings',
            'data': False
        }
        return jsonify(response_object), 400

    @staticmethod
    def invalid_data_type():
        response_object = {
            'status': '400',
            'error_message': 'Please an integer is needed here',
            'data': False
        }
        return jsonify(response_object), 400

    @staticmethod
    def empty_data_fields():
        response_object = {
            'status': '400',
            'error_message': 'Some fields have no data',
            'data': False
        }
        return jsonify(response_object), 400

    @staticmethod
    def empty_data_storage():
        response_object = {
            'status': '200',
            'message': 'No records currently',
            'data': False
        }
        return jsonify(response_object), 200

    @staticmethod
    def no_redflag():
        response_object = {
            'status': '404',
            'error_message': 'redflag does not exist',
            'data': False
        }
        return jsonify(response_object), 400

    @staticmethod
    def missing_key(keys):
        response_object = {

            'Blank space': 'You have missing feilds '

        }
        return jsonify(response_object), 400

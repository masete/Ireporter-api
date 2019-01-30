import datetime
from functools import wraps
import jwt
from flask import request, jsonify

secret_key = "masete_you"


def encode_token(user_id, is_admin=0):
    payload = {
        "user_id": user_id,
        "is_Admin": is_admin,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=3),
    }
    token = jwt.encode(payload, secret_key, algorithm="HS256").decode("utf-8")

    return token


def decode_token(token):
    decoded = jwt.decode(str(token), secret_key, algorithm="HS256")
    return decoded


def extract_token_from_header():
    authorizaton_header = request.headers.get("Authorization")
    if not authorizaton_header or "Bearer" not in authorizaton_header:
        return (
            jsonify({"error": "Bad authorization header", "status": 400}),
            400,
        )
    token = str(authorizaton_header).split(" ")[1]
    return token


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = None
        try:
            token = extract_token_from_header()
            decode_token(token)
            response = func(*args, **kwargs)

        except jwt.ExpiredSignatureError:
            response = (
                jsonify({"error": "token has expired", "status": 401}),
                401,
            )
        except jwt.InvalidTokenError:
            response = (
                jsonify({"error": "token input is invalid", "status": 401}),
                401,
            )
        return response

    return wrapper


def get_current_identity():
    return decode_token(extract_token_from_header())["userid"]


def get_current_role():
    return decode_token(extract_token_from_header())["is_Admin"]


def non_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if get_current_role():
            return (
                jsonify(
                    {
                        "error": "Admin cannot access this resource",
                        "status": 403,
                    }
                ),
                403,
            )
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not get_current_role():
            return (
                jsonify(
                    {
                        "error": "Only Admin can access this resource",
                        "status": 403,
                    }
                ),
                403,
            )
        return func(*args, **kwargs)

    return wrapper

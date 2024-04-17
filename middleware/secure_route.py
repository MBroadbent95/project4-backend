from http import HTTPStatus
from functools import wraps
from flask import request, g
import jwt

from app import db
from models.user import UserModel

from config.environment import SECRET


def secure_route(route_func):

    @wraps(route_func)
    def wrapper(*args, **kwargs):

        raw_token = request.headers.get("Authorization")
        print(raw_token)

        if not raw_token:
            print("Token is not there.")
            return {
                "message": "Unauthorized: Token is misssing"
            }, HTTPStatus.UNAUTHORIZED

        token = raw_token.replace("Bearer ", "")
        print(token)

        try:
            payload = jwt.decode(token, SECRET, algorithms=["HS256"])
            print("Decoded payload:", payload)
            print("Token was valid")

            user_id = payload["sub"]

            if not user_id:
                return {
                    "message": "Unauthorized: Invalid token payload"
                }, HTTPStatus.UNAUTHORIZED

            user = db.session.query(UserModel).get(user_id)

            g.current_user = user

            print("current user is: ", g.current_user.username, g.current_user.id)
            print(payload)
            return route_func(*args, **kwargs)

        except jwt.ExpiredSignatureError:
            print("Expired")
            return {"message": "Token has expired"}, HTTPStatus.UNAUTHORIZED
        except jwt.InvalidTokenError as e:
            return {
                "message": f"Unauthorized: Invalid Token: {str(e)}"
            }, HTTPStatus.UNAUTHORIZED
        except Exception as e:
            print(e)
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

    return wrapper

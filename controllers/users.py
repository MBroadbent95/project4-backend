from http import HTTPStatus

from datetime import datetime, timezone, timedelta

from flask import Blueprint, request

from marshmallow.exceptions import ValidationError

from app import db

from models.user import UserModel

from serializers.user import UserSerializer

import jwt

from config.environment import SECRET


user_serializer = UserSerializer()

router = Blueprint("users", __name__)


@router.route("/signup", methods=["POST"])
def signup():
    user_dictionary = request.json

    if user_dictionary["password"] != user_dictionary["passwordConfirmation"]:
        return {
            "errors": "Passwords do not match",
            "messsages": "Something went wrong",
        }, HTTPStatus.UNPROCESSABLE_ENTITY

    # ! Delete the password conf field that marshmallow doens't know about.
    del user_dictionary["password_confirmation"]
    try:

        print("in signup", user_dictionary)

        user_model = user_serializer.load(user_dictionary)

        db.session.add(user_model)
        db.session.commit()

        print("user model", user_model.password)

        return user_serializer.jsonify(user_model)

    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        print(e)
        return {"message": "Something went wrong"}, HTTPStatus.INTERNAL_SERVER_ERROR


@router.route("/login", methods=["POST"])
def login():

    credentials_dictionary = request.json

    user = (
        db.session.query(UserModel)
        .filter_by(email=credentials_dictionary["email"])
        .first()
    )

    if not user:
        return {"message": "Login failed. Try again."}, 401

    if not user.validate_password(credentials_dictionary["password"]):
        return {"message": "Login failed. Try again."}, 401

    payload = {
        "exp": datetime.now(timezone.utc) + timedelta(days=2),
        "iat": datetime.now(timezone.utc),
        "sub": user.id,
    }

    token = jwt.encode(
        payload,
        SECRET,
        algorithm="HS256",
    )
    print("Otherwise success!!")

    return {"message": "Login Successful", "token": token}, 200


@router.route("/user", methods=["GET"])
def get_current_user():
    # Retrieve the JWT token from the request headers
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return {"message": "Authorization header is missing"}, HTTPStatus.UNAUTHORIZED

    # Extract the token from the Authorization header
    token = auth_header.split(" ")[1]

    try:
        # Decode the token using the secret key
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        # Extract the user id from the decoded payload
        user_id = payload["sub"]

        # Retrieve the user from the database based on the user id
        # user = UserModel.query.get(user_id)
        user = db.session.query(UserModel).get(user_id)

        if not user:
            return {"message": "User not found"}, HTTPStatus.NOT_FOUND

        # Serialize the user data
        serialized_user = user_serializer.dump(user)

        return serialized_user, HTTPStatus.OK

    except jwt.ExpiredSignatureError:
        return {"message": "Token has expired"}, HTTPStatus.UNAUTHORIZED

    except jwt.InvalidTokenError:
        return {"message": "Invalid token"}, HTTPStatus.UNAUTHORIZED

    except Exception as e:
        print(e)
        return {"message": "Something went wrong"}, HTTPStatus.INTERNAL_SERVER_ERROR

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

    try:
        user_dictionary = request.json

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

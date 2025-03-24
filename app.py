from dotenv import load_dotenv

import os

from flask import Flask, jsonify

from flask_cors import CORS

# from config.environment import db_URI

from extensions import db, marsh, bcrypt

load_dotenv()

db_URI = os.getenv("DATABASE_URL")

SECRET_KEY = os.getenv("SECRET")


def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = db_URI
    app.config["SECRET_KEY"] = SECRET_KEY

    CORS(
        app,
        origins=[
            "https://tasteful-trove.netlify.app",
        ],
    )

    db.init_app(app)
    marsh.init_app(app)
    bcrypt.init_app(app)

    @app.route("/", methods=["GET"])
    def home():
        return "Welcome to the Project 4 Backend!"

    @app.route("/hello", methods=["GET"])
    def hello():
        return "Hello, World!"

    with app.app_context():
        from seed import seed_database

        seed_database()

    from controllers import recipes, users

    app.register_blueprint(recipes.router, url_prefix="/api")
    app.register_blueprint(users.router, url_prefix="/api")

    return app


app = create_app()

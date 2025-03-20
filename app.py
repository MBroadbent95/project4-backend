from flask import Flask, jsonify

from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow

from flask_bcrypt import Bcrypt

from config.environment import db_URI

from flask_cors import CORS

from seed import seed_database


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Project 4 Backend!"


@app.route("/hello", methods=["GET"])
def hello():
    return "Hello, World!"


@app.route("/seed", methods=["POST"])
def seed_data():
    try:
        # Call your seeding function here
        seed_database()
        return jsonify({"message": "Database seeded successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


app.config["SQLALCHEMY_DATABASE_URI"] = db_URI

CORS(app)

db = SQLAlchemy(app)

marsh = Marshmallow(app)

bcrypt = Bcrypt(app)

with app.app_context():
    seed_database()


from controllers import recipes, users

app.register_blueprint(recipes.router, url_prefix="/api")
app.register_blueprint(users.router, url_prefix="/api")

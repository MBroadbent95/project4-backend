from app import db

from models.user import UserModel


class RecipeModel(db.Model):

    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Text, nullable=False, unique=True)
    serving = db.Column(db.Text, nullable=False)
    prep_time = db.Column(db.Text, nullable=False)
    total_time = db.Column(db.Text, nullable=False)
    cal_serv = db.Column(db.Integer, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    directions_instructions = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("UserModel", backref="recipes")

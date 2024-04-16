from app import db
from models.base import BaseModel


class CommentModel(db.Model, BaseModel):

    __tablename__ = "comments"

    content = db.Column(db.Text, nullable=False)

    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("UserModel", backref="comments")

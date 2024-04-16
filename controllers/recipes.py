from http import HTTPStatus

from flask import Blueprint, request, g

from marshmallow.exceptions import ValidationError

from sqlalchemy.exc import SQLAlchemyError

from models.comment import CommentModel

from models.recipe import RecipeModel

from app import db


from middleware.secure_route import secure_route

from serializers.recipe import RecipeSerializer
from serializers.comment import CommentSchema

recipe_serializer = RecipeSerializer()

comment_schema = CommentSchema()

router = Blueprint("recipes", __name__)


@router.route("/recipes", methods=["GET"])
def get_recipes():
    try:

        recipes = db.session.query(RecipeModel).all()
        return recipe_serializer.jsonify(recipes, many=True)
    except SQLAlchemyError as e:
        return str(e), 500


@router.route("/recipes/<int:recipe_id>", methods=["GET"])
def get_single_recipe(recipe_id):
    try:

        recipe = db.session.query(RecipeModel).get(recipe_id)
        if recipe:
            return recipe_serializer.jsonify(recipe)
        else:
            return "Recipe not found", 404
    except SQLAlchemyError as e:
        return str(e), 500


@router.route("/recipes", methods=["POST"])
@secure_route
def create():
    try:
        recipe_dictionary = request.json

        recipe_model = recipe_serializer.load(recipe_dictionary)

        recipe_model.user_id = g.current_user.id

        db.session.add(recipe_model)
        db.session.commit()

        return recipe_serializer.jsonify(recipe_model)
    except SQLAlchemyError as e:
        return str(e), 500


@router.route("/recipes/<int:recipe_id>", methods=["DELETE"])
@secure_route
def delete_recipe(recipe_id):
    try:

        recipe = db.session.query(RecipeModel).get(recipe_id)

        if recipe:
            db.session.delete(recipe)
            db.session.commit()
            return "Recipe deleted successfully", 200
        else:
            return "Recipe not found", 404
    except SQLAlchemyError as e:
        return str(e), 500


@router.route("/recipes/<int:recipe_id>", methods=["PUT"])
@secure_route
def update_recipe(recipe_id):
    try:

        recipe = db.session.query(RecipeModel).get(recipe_id)

        if recipe:
            updated_data = request.json
            for key, value in updated_data.items():
                setattr(recipe, key, value)
            db.session.commit()
            return recipe_serializer.jsonify(recipe)
        else:
            return "Recipe not found", 404
    except SQLAlchemyError as e:
        return str(e), 500


@router.route("/recipes/<int:recipe_id>/comments", methods=["POST"])
@secure_route
def create_comment(recipe_id):

    comment_dictionary = request.json

    existing_recipe = RecipeModel.query.get(recipe_id)
    if not existing_recipe:
        return {"message": "No recipe found"}, HTTPStatus.NOT_FOUND

    try:
        comment = comment_schema.load(comment_dictionary)
        comment.recipe_id = recipe_id
        comment.save()
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}

    return comment_schema.jsonify(comment), HTTPStatus.CREATED


@router.route("/comments/<int:comment_id>", methods=["DELETE"])
@secure_route
def remove_comment(comment_id):

    comment = CommentModel.query.get(comment_id)

    if not comment:
        return {"message": "No comment found"}, HTTPStatus.NOT_FOUND

    if comment.user_id != g.current_user.id:
        return {
            "message": "You are not authorized to delete this comment"
        }, HTTPStatus.FORBIDDEN

    comment.remove()

    return "", HTTPStatus.NO_CONTENT


@router.route("/recipes/<int:recipe_id>/comments", methods=["GET"])
def get_comments_for_recipe(recipe_id):
    recipe = RecipeModel.query.get(recipe_id)
    if not recipe:
        return {"message": "Recipe not found"}, HTTPStatus.NOT_FOUND

    comments = recipe.comments.all()  # Access comments associated with the recipe

    return comment_schema.jsonify(comments, many=True), HTTPStatus.OK

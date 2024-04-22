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
from serializers.superComment import SuperCommentSchema

recipe_serializer = RecipeSerializer()

super_comment_schema = SuperCommentSchema()

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
    recipe_dictionary = request.json

    if "name" not in recipe_dictionary or not recipe_dictionary["name"]:
        return {"errors": {"name": "Name field is required."}}, 400

    if "cuisine" not in recipe_dictionary or not recipe_dictionary["cuisine"]:
        return {"errors": {"cuisine": "Cuisine field is required."}}, 400

    if "serving" not in recipe_dictionary or not recipe_dictionary["serving"]:
        return {"errors": {"serving": "Serving field is required."}}, 400

    if "prep_time" not in recipe_dictionary or not recipe_dictionary["prep_time"]:
        return {"errors": {"prep_time": "Prep Time field is required."}}, 400

    if "total_time" not in recipe_dictionary or not recipe_dictionary["total_time"]:
        return {"errors": {"total_time": "Total Time field is required."}}, 400

    if "cal_serv" not in recipe_dictionary or not recipe_dictionary["cal_serv"]:
        return {"errors": {"cal_serv": "Cal Serv field is required."}}, 400

    if "ingredients" not in recipe_dictionary or not recipe_dictionary["ingredients"]:
        return {"errors": {"ingredients": "Ingredients field is required."}}, 400
    if (
        "directions_instructions" not in recipe_dictionary
        or not recipe_dictionary["directions_instructions"]
    ):
        return {
            "errors": {
                "directions_instructions": "Directions Instructions field is required."
            }
        }, 400
    if "image_url" not in recipe_dictionary or not recipe_dictionary["image_url"]:
        return {"errors": {"image_url": "image Url field is required."}}, 400
    try:

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

        comment = super_comment_schema.load(comment_dictionary)
        print(comment_dictionary)
        comment.user_id = g.current_user.id
        comment.recipe_id = recipe_id
        comment.save()

    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}

    return super_comment_schema.jsonify(comment), HTTPStatus.CREATED


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

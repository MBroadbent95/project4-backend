from app import marsh

from models.recipe import RecipeModel

from marshmallow import fields

from serializers.user import UserSerializer


class RecipeSerializer(marsh.SQLAlchemyAutoSchema):

    user = fields.Nested("UserSerializer", many=False)

    class Meta:

        model = RecipeModel

        load_instance = True
        include_fk = True

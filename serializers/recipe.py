from app import marsh

from models.crisp import CrispModel

from marshmallow import fields

from serializers.user import UserSerializer


class CrispSerializer(marsh.SQLAlchemyAutoSchema):

    user = fields.Nested("UserSerializer", many=False)

    class Meta:

        model = CrispModel

        load_instance = True

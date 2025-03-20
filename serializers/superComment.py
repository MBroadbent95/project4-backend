from extensions import marsh
from models.comment import CommentModel


class SuperCommentSchema(marsh.SQLAlchemyAutoSchema):

    class Meta:
        model = CommentModel
        load_instance = True

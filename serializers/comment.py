from app import marsh
from models.comment import CommentModel


class CommentSchema(marsh.SQLAlchemyAutoSchema):

    class Meta:
        model = CommentModel
        load_instance = True
        include_fk = True

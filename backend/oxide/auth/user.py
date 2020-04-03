from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from oxide.core.database import db, AbstractModel


class User(AbstractModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))


# class UserSchema(BaseSchema):
#     class Meta:
#         model = User


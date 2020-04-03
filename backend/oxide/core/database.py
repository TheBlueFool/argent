from .extensions import db, ma


class AbstractModel(db.Model):
    """Base model class."""

    __abstract__ = True


class BaseSchema(ma.SQLAlchemySchema):
    class Meta:
        sqla_session = db.session

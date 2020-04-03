from marshmallow_sqlalchemy import SQLAlchemySchemaOpts, SQLAlchemySchema
from .extensions import db


class AbstractModel(db.Model):
    """Base model class."""

    __abstract__ = True




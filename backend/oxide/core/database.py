from .extensions import db


class Model(db.Model):
    """Base model class."""

    __abstract__ = True

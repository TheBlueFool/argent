from oxide.core.database import db, Model


class User(Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

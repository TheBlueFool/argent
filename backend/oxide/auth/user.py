from flask_login import UserMixin
from oxide import login_manager
from oxide.core.database import db, ma

from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

    id = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()
    password_hash = ma.auto_field()

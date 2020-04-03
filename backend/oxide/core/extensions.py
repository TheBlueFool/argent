"""Extensions module.
Each extension is initialized in the app factory located in app.py."""
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

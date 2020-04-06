import pytest

from oxide.core.extensions import db
from oxide import create_app
from oxide.core.config_skeleton import Config


class TestConfig(Config):
    TESTING = True
    SECRET_KEY = "test"
    SQLALCHEMY_DATABASE_URI = "sqlite://"


@pytest.fixture(scope="session")
def app():
    """
    Fixture for integration with pytest-flask
    :return:
    """
    _app = create_app(TestConfig)
    # create the database and load test data
    with _app.app_context():
        db.create_all()
        yield _app
        db.drop_all()


@pytest.fixture(scope="session")
def _db(app):
    """
    Fixture for integration with pytest-flask-sqlalchemy
    :param app:
    :return:
    """
    db.create_all()
    yield db
    db.drop_all()

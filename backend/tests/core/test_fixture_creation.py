def test_app_creates(app):
    assert app


# pytest_flask.fixtures


def test_live_server_fixture(live_server):
    assert live_server


def test_config_fixture(config):
    assert config


def test_request_ctx_fixture(request_ctx):
    assert request_ctx


def test_client_fixture(client):
    assert client


#  fixtures defined from pytest_flask_sqlalchemy.fixtures


def test_db_session_fixture(db_session):
    assert db_session


def test_db_engine_fixture(db_engine):
    assert db_engine

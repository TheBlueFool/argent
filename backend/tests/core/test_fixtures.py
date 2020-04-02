import pytest


@pytest.mark.unit
@pytest.mark.compile
def test_app_creates(app):
    assert app


@pytest.mark.unit
@pytest.mark.compile
def test_live_server_fixture(live_server):
    assert live_server


@pytest.mark.unit
@pytest.mark.compile
def test_config_fixture(config):
    assert config


@pytest.mark.unit
@pytest.mark.compile
def test_request_ctx_fixture(request_ctx):
    assert request_ctx


@pytest.mark.unit
@pytest.mark.compile
def test_client_fixture(client):
    assert client


@pytest.mark.unit
@pytest.mark.compile
def test_db_session_fixture(db_session):
    assert db_session


@pytest.mark.unit
@pytest.mark.compile
def test_db_engine_fixture(db_engine):
    assert db_engine

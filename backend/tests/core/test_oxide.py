import pytest


# @pytest.mark.unit
# @pytest.mark.compile
# def test_empty_db(client):
#     """Start with a blank database."""
#     rv = client.get("/")
#     assert b"Hello, World!" in rv.data


@pytest.mark.compile
def test_flask_app_config_is_testing(app):
    assert app.config["TESTING"] == True


@pytest.mark.integration
@pytest.mark.commit
def test_integration(app):
    pass


@pytest.mark.unit
@pytest.mark.compile
def test_hello(client):
    response = client.get("/hello")
    assert response.data == b"Hello, World!"


@pytest.mark.unit
@pytest.mark.compile
def test_root_hello(client):
    response = client.get("/")
    assert response.data == b"Hello, World!"

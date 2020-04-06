def test_flask_app_config_is_testing(app):
    assert app.config["TESTING"] is True

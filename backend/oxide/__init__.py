# -*- coding: utf-8 -*-
import ddtrace
import logging
import os
import sys
from flask import Flask

from oxide.core.extensions import db, login_manager, ma, migrate


def create_app(config_object=None):
    """Application factory for Oxide

    :param config_object: Fully populated configuration object used to build app
    """
    # Initialize the core application
    app = Flask(__name__)
    _load_config(app, config_object)
    _init_app(app)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    login_manager.init_app(app)

    # Initialize packages and Blueprints
    with app.app_context():
        from oxide.basic_features import load_basic_features_package
        from oxide.core import load_core_package
        from oxide.cli import load_cli_package
        from oxide.auth import load_auth_package

        @app.route("/force")
        def hello_world():
            return "Hello, World!"

        load_core_package(app)
        load_basic_features_package(app)
        load_cli_package(app)
        load_auth_package(app)

    return app


def _load_config(app, config_object):
    if config_object is None:
        from oxide.core.config_skeleton import Config
        from oxide.core.constants import CONFIG_PATH_ENV_VAR

        app.config.from_object(Config)
        app.config.from_envvar(CONFIG_PATH_ENV_VAR)
    else:
        app.config.from_object(config_object)


def _init_app(app):
    app.url_map.strict_slashes = False
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)

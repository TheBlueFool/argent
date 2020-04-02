from flask import Blueprint

api_v0_bp = Blueprint("api", __name__)


def load_api_v0_package(app):

    app.register_blueprint(api_v0_bp, url_prefix="/api/v0")

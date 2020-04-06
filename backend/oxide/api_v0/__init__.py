from oxide.api_v0.routes import api_v0_bp


def load_api_v0_package(app):

    app.register_blueprint(api_v0_bp, url_prefix="/api/v0")

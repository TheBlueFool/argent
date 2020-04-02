from .routes import basic_bp


def load_basic_features_package(app):
    app.register_blueprint(basic_bp)

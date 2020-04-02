from .handlers import bp


def load_core_package(app):
    app.register_blueprint(bp)

from oxide.flower.routes import flowers_bp


def load_flower_package(app):
    # import models
    from oxide.flower.models import Flower

    # import routes via blueprint
    app.register_blueprint(flowers_bp)

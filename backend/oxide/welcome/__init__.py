from oxide.welcome.routes import welcome_bp


def load_welcome_packeage(app):
    app.register_blueprint(welcome_bp)

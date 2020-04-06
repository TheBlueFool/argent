import click
from flask.cli import with_appcontext

from oxide.flower.models import Flower, FlowerFactory, FlowerSchema
from oxide.cli.test import register_tests
from oxide.core.extensions import db


def load_cli_package(app):
    _register_single_commands(app)
    register_tests(app, db)

    @app.shell_context_processor
    def make_shell_context():
        flower_schema = FlowerSchema()

        return {
            "db": db,
            "Flower": Flower,
            "flower_schema": flower_schema,
            "FlowerFactory": FlowerFactory,
        }


@click.command()
@with_appcontext
def zap():
    pass


@click.command()
@with_appcontext
def lint():
    """Lint and Format"""
    click.echo("noop")
    click.echo("WIP")


@click.command()
@with_appcontext
def init():
    """Initialize a development DB and workspace """
    from flask_migrate import upgrade

    upgrade()
    db.session.commit()
    click.echo("Initialized the database.")


def _register_single_commands(app):
    app.cli.add_command(zap)
    app.cli.add_command(lint)
    app.cli.add_command(init)

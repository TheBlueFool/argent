import click


def register_tests(app, db):
    @app.cli.group()
    def test():
        """Run all unit and integration tests"""
        click.echo("noop")
        click.echo("WIP")

    @test.command()
    def short():
        """Run only unit tests"""
        click.echo("noop")
        click.echo("WIP")

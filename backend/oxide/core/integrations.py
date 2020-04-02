import ddtrace
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration


def configure_sentry(app):
    sentry_sdk.init(
        dsn=app.config["SENTRY_DSN"],
        integrations=[FlaskIntegration(), SqlalchemyIntegration()],
        environment=app.config["ENV"],
    )


def configure_datadog(app):
    pass

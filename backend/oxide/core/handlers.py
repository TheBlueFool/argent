from flask import Blueprint

from oxide.core.extensions import db

bp = Blueprint("errors", __name__)


@bp.app_errorhandler(404)
def not_found_error(error):
    return "some text", 404


@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return "500", 500

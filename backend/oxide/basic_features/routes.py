from flask_login import login_required
from flask import Blueprint

basic_bp = Blueprint("basic_features", __name__)


@basic_bp.route("/", methods=["GET", "POST"])
def index():
    return "Hello, World!"


@basic_bp.route("/hello", methods=["GET", "POST"])
def index_hello():
    return "Hello, World!"


@basic_bp.route("/debug-sentry")
def trigger_error():
    division_by_zero = 1 / 0
    return division_by_zero


def _build_debug_json():
    pass


@basic_bp.route("/secret")
@login_required
def secret():
    return "Only authenticated users are allowed!"


@basic_bp.route("/debug")
@basic_bp.route("/debug/")
def surface_debug_info():
    response = _build_debug_json()
    return response, 200

from flask import Blueprint

basic_bp = Blueprint("basic_features", __name__)


@basic_bp.route("/hw", methods=["GET", "POST"])
def index_hello():
    return "Hello, World!"


@basic_bp.route("/debug-sentry")
def trigger_error():
    division_by_zero = 1 / 0
    return division_by_zero


def _build_debug_json():
    pass


@basic_bp.route("/debug")
@basic_bp.route("/debug/")
def surface_debug_info():
    return _build_debug_json(), 200

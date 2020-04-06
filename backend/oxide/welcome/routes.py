from flask import Blueprint
from flask import jsonify

from oxide.welcome.greeting import make_greeting

welcome_bp = Blueprint("welcome", __name__)


@welcome_bp.route("/hello", methods=["GET"])
@welcome_bp.route("/hello/<string:name>", methods=["GET"])
def get_welcome_detail(name=None):
    return jsonify(make_greeting(name))

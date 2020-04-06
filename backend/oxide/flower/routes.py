from flask import Blueprint
from flask import request

from oxide import db
from oxide.flower.models import Flower, flower_schema, flowers_schema

flowers_bp = Blueprint("flowers", __name__)


@flowers_bp.route("/flowers/<int:id>", methods=["GET"])
def get_flower_detail(id):
    user = Flower.get(id)
    return flower_schema.dump(user)


@flowers_bp.route("/flowers", methods=["GET"])
def get_flowers():
    # all_users = current_app.db.session.query(Flower).all()
    all_users = Flower.query.all()
    return flowers_schema.jsonify(all_users)


@flowers_bp.route("/flowers", methods=["POST"])
def create_flower():
    json_data = request.get_json() or {}
    # # Validate and deserialize input
    errors = flower_schema.validate(json_data)
    if errors:
        return errors, 422
    flower = flower_schema.load(json_data)
    # flower = Flower.query.filter_by(name=data['id']).first()
    # if flower:
    #     return {'message': 'Flower already exists'}, 400
    # flower = Flower(
    #     name=json_data['name']
    # )
    db.session.add(flower)
    db.session.commit()

    result = flower_schema.dump(flower)

    return {"status": "success", "data": result}, 201


@flowers_bp.route("/flowers/<int:id>", methods=["PUT"])
def update_flower(id):
    pass

from flask import Blueprint, jsonify,request
from app.models.store_model import Store
from app.ultis.decorator import jwt_required, roles_required
from app.views.store_view import render_store_detail,render_store_list

store_bp=Blueprint("store",__name__)


@store_bp.route("stores/",methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_stores():
    stores=Store.get_all()
    return jsonify(render_store_list(stores))

@store_bp.route("/stores/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_Store(id):
    Store = Store.get_by_id(id)
    if Store:
        return jsonify(render_store_detail(Store))
    return jsonify({"error": "Store no encontrado"}), 404


@store_bp.route("/stores", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_Store():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock=data.get("stock")

    if not name or not description or not price or stock is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    Store = Store(name=name, description=description, price=price,stock=stock)
    Store.save()

    return jsonify(render_store_detail(Store)), 201


@store_bp.route("/stores/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_Store(id):
    Store = Store.get_by_id(id)
    if not Store:
        return jsonify({"error": "Store no encontrado"}), 404
    data = request.json
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")

    Store.update(name=name, description=description, price=price)

    return jsonify(render_store_detail(Store))


@store_bp.route("/stores/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_Store(id):
    Store = Store.get_by_id(id)

    if not Store:
        return jsonify({"error": "Store no encontrado"}), 404

    Store.delete()

    return "", 204

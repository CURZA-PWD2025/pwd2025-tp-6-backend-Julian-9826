from flask import Blueprint, request, jsonify
from .ArticuloController import ArticuloController

articulos_bp = Blueprint("articulos_bp", __name__)

@articulos_bp.route("/articulos", methods=["GET"])
def get_all():
    return jsonify(ArticuloController.get_all())

@articulos_bp.route("/articulos/<int:id>", methods=["GET"])
def get_one(id):
    return jsonify(ArticuloController.get_one(id))

@articulos_bp.route("/articulos", methods=["POST"])
def create():
    data = request.json
    return jsonify(ArticuloController.create(data))

@articulos_bp.route("/articulos/<int:id>", methods=["PUT"])
def update(id):
    data = request.json
    data["id"] = id
    return jsonify(ArticuloController.update(data))

@articulos_bp.route("/articulos/<int:id>", methods=["DELETE"])
def delete(id):
    return jsonify(ArticuloController.delete(id))

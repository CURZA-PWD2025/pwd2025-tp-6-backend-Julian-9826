from flask import Blueprint, request, jsonify
from .CategoriaController import CategoriaController

categorias_bp = Blueprint("categorias_bp", __name__)

@categorias_bp.route("/categorias", methods=["GET"])
def get_all():
    return jsonify(CategoriaController.get_all())

@categorias_bp.route("/categorias/<int:id>", methods=["GET"])
def get_one(id):
    return jsonify(CategoriaController.get_one(id))

@categorias_bp.route("/categorias", methods=["POST"])
def create():
    data = request.json
    return jsonify(CategoriaController.create(data))

@categorias_bp.route("/categorias/<int:id>", methods=["PUT"])
def update(id):
    data = request.json
    data["id"] = id
    return jsonify(CategoriaController.update(data))

@categorias_bp.route("/categorias/<int:id>", methods=["DELETE"])
def delete(id):
    return jsonify(CategoriaController.delete(id))

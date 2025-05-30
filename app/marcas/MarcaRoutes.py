from flask import Blueprint, request, jsonify
from .MarcaController import MarcaController

marcas_bp = Blueprint("marcas_bp", __name__)

@marcas_bp.route("/marcas", methods=["GET"])
def get_all():
    return jsonify(MarcaController.get_all())

@marcas_bp.route("/marcas/<int:id>", methods=["GET"])
def get_one(id):
    return jsonify(MarcaController.get_one(id))

@marcas_bp.route("/marcas", methods=["POST"])
def create():
    data = request.json
    return jsonify(MarcaController.create(data))

@marcas_bp.route("/marcas/<int:id>", methods=["PUT"])
def update(id):
    data = request.json
    data["id"] = id
    return jsonify(MarcaController.update(data))

@marcas_bp.route("/marcas/<int:id>", methods=["DELETE"])
def delete(id):
    return jsonify(MarcaController.delete(id))

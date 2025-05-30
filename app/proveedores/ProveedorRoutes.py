from flask import Blueprint, request, jsonify
from .ProveedorController import ProveedorController

proveedores_bp = Blueprint("proveedores_bp", __name__)

@proveedores_bp.route("/proveedores", methods=["GET"])
def get_all():
    return jsonify(ProveedorController.get_all())

@proveedores_bp.route("/proveedores/<int:id>", methods=["GET"])
def get_one(id):
    return jsonify(ProveedorController.get_one(id))

@proveedores_bp.route("/proveedores", methods=["POST"])
def create():
    data = request.json
    return jsonify(ProveedorController.create(data))

@proveedores_bp.route("/proveedores/<int:id>", methods=["PUT"])
def update(id):
    data = request.json
    data["id"] = id
    return jsonify(ProveedorController.update(data))

@proveedores_bp.route("/proveedores/<int:id>", methods=["DELETE"])
def delete(id):
    return jsonify(ProveedorController.delete(id))

from flask import Blueprint, request, jsonify
from .ProveedorController import (
    crear_proveedor,
    obtener_proveedores,
    obtener_proveedor_por_id,
    actualizar_proveedor,
    eliminar_proveedor
)

proveedores_bp = Blueprint("proveedores_bp", __name__, url_prefix="/proveedores")

# Crear un proveedor
@proveedores_bp.route("", methods=["POST"])
def crear():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Faltan datos"}), 400
    proveedor = crear_proveedor(data)
    return jsonify(proveedor), 201

# Obtener todos los proveedores
@proveedores_bp.route("", methods=["GET"])
def listar():
    proveedores = obtener_proveedores()
    return jsonify(proveedores), 200

# Obtener proveedor por ID
@proveedores_bp.route("/<int:proveedor_id>", methods=["GET"])
def obtener(proveedor_id):
    proveedor = obtener_proveedor_por_id(proveedor_id)
    if proveedor:
        return jsonify(proveedor), 200
    return jsonify({"error": "Proveedor no encontrado"}), 404

# Actualizar proveedor
@proveedores_bp.route("/<int:proveedor_id>", methods=["PUT"])
def actualizar(proveedor_id):
    data = request.get_json()
    proveedor = actualizar_proveedor(proveedor_id, data)
    if proveedor:
        return jsonify(proveedor), 200
    return jsonify({"error": "Proveedor no encontrado"}), 404

# Eliminar proveedor
@proveedores_bp.route("/<int:proveedor_id>", methods=["DELETE"])
def eliminar(proveedor_id):
    if eliminar_proveedor(proveedor_id):
        return jsonify({"mensaje": "Proveedor eliminado"}), 200
    return jsonify({"error": "Proveedor no encontrado"}), 404

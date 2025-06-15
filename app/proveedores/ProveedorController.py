from app.db import db

from .ProveedorModel import ProveedorModel

def crear_proveedor(data):
    nuevo = ProveedorModel(
        nombre=data["nombre"],
        telefono=data["telefono"],
        direccion=data["direccion"],
        email=data["email"]
    )
    db.session.add(nuevo)
    db.session.commit()
    return nuevo.serializar()

def obtener_proveedores():
    return ProveedorModel.get_all()

def obtener_proveedor_por_id(proveedor_id):
    return ProveedorModel.get_one(proveedor_id)

def actualizar_proveedor(proveedor_id, data):
    proveedor = ProveedorModel.query.get(proveedor_id)
    if proveedor:
        proveedor.update(data)
        db.session.commit()
        return proveedor.serializar()
    return None

def eliminar_proveedor(proveedor_id):
    return ProveedorModel.delete(proveedor_id)

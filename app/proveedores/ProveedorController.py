from .ProveedorModel import ProveedorModel

class ProveedorController:

    @staticmethod
    def get_all():
        return ProveedorModel.get_all()

    @staticmethod
    def get_one(id):
        return ProveedorModel.get_one(id)

    @staticmethod
    def create(data):
        nuevo = ProveedorModel.deserializar(data)
        ProveedorModel.db.append(nuevo)
        return nuevo.serializar()

    @staticmethod
    def update(data):
        for p in ProveedorModel.db:
            if p.id == data.get("id"):
                p.update(data)
                return p.serializar()
        return {"error": "Proveedor no encontrado"}

    @staticmethod
    def delete(id):
        if ProveedorModel.delete(id):
            return {"mensaje": "Proveedor eliminado"}
        return {"error": "Proveedor no encontrado"}

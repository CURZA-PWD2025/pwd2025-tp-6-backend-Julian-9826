from .CategoriaModel import CategoriaModel

class CategoriaController:

    @staticmethod
    def get_all():
        return CategoriaModel.get_all()

    @staticmethod
    def get_one(id):
        return CategoriaModel.get_one(id)

    @staticmethod
    def create(data):
        nueva = CategoriaModel.deserializar(data)
        CategoriaModel.db.append(nueva)
        return nueva.serializar()

    @staticmethod
    def update(data):
        for c in CategoriaModel.db:
            if c.id == data.get("id"):
                c.update(data)
                return c.serializar()
        return {"error": "Categoría no encontrada"}

    @staticmethod
    def delete(id):
        if CategoriaModel.delete(id):
            return {"mensaje": "Categoría eliminada"}
        return {"error": "Categoría no encontrada"}

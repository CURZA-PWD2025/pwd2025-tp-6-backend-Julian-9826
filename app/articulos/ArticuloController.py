from .ArticuloModel import ArticuloModel

class ArticuloController:

    @staticmethod
    def get_all():
        return ArticuloModel.get_all()

    @staticmethod
    def get_one(id):
        return ArticuloModel.get_one(id)

    @staticmethod
    def create(data):
        nuevo = ArticuloModel.deserializar(data)
        ArticuloModel.db.append(nuevo)
        return nuevo.serializar()

    @staticmethod
    def update(data):
        for a in ArticuloModel.db:
            if a.id == data.get("id"):
                a.update(data)
                return a.serializar()
        return {"error": "Artículo no encontrado"}

    @staticmethod
    def delete(id):
        if ArticuloModel.delete(id):
            return {"mensaje": "Artículo eliminado"}
        return {"error": "Artículo no encontrado"}

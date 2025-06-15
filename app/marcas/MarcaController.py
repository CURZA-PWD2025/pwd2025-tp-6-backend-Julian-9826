from .MarcaModel import MarcaModel

class MarcaController:

    @staticmethod
    def get_all():
        return MarcaModel.get_all()

    @staticmethod
    def get_one(id):
        return MarcaModel.get_one(id)

    @staticmethod
    def create(data):
        nueva = MarcaModel.deserializar(data)
        MarcaModel.db.append(nueva)
        return nueva.serializar()

    @staticmethod
    def update(data):
        for m in MarcaModel.db:
            if m.id == data.get("id"):
                m.update(data)
                return m.serializar()
        return {"error": "Marca no encontrada"}

    @staticmethod
    def delete(id):
        if MarcaModel.delete(id):
            return {"mensaje": "Marca eliminada"}
        return {"error": "Marca no encontrada"}

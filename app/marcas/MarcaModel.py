class MarcaModel:
    db = []
    id_counter = 1

    def __init__(self, descripcion):
        self.id = MarcaModel.id_counter
        MarcaModel.id_counter += 1
        self.descripcion = descripcion

    def serializar(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion
        }

    @staticmethod
    def deserializar(data):
        return MarcaModel(descripcion=data.get("descripcion"))

    def update(self, data):
        self.descripcion = data.get("descripcion", self.descripcion)
        return True

    @staticmethod
    def get_all():
        return [m.serializar() for m in MarcaModel.db]

    @staticmethod
    def get_one(id):
        for m in MarcaModel.db:
            if m.id == id:
                return m.serializar()
        return None

    @staticmethod
    def delete(id):
        for i, m in enumerate(MarcaModel.db):
            if m.id == id:
                del MarcaModel.db[i]
                return True
        return False

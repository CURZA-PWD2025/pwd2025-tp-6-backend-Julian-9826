class CategoriaModel:
    db = []
    id_counter = 1

    def __init__(self, descripcion):
        self.id = CategoriaModel.id_counter
        CategoriaModel.id_counter += 1
        self.descripcion = descripcion

    def serializar(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion
        }

    @staticmethod
    def deserializar(data):
        return CategoriaModel(descripcion=data.get("descripcion"))

    def update(self, data):
        self.descripcion = data.get("descripcion", self.descripcion)
        return True

    @staticmethod
    def get_all():
        return [c.serializar() for c in CategoriaModel.db]

    @staticmethod
    def get_one(id):
        for c in CategoriaModel.db:
            if c.id == id:
                return c.serializar()
        return None

    @staticmethod
    def delete(id):
        for i, c in enumerate(CategoriaModel.db):
            if c.id == id:
                del CategoriaModel.db[i]
                return True
        return False

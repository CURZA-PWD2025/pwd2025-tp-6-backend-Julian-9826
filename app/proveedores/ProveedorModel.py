class ProveedorModel:
    db = []
    id_counter = 1

    def __init__(self, nombre, telefono, direccion, email):
        self.id = ProveedorModel.id_counter
        ProveedorModel.id_counter += 1
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

    def serializar(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "email": self.email
        }

    @staticmethod
    def deserializar(data):
        return ProveedorModel(
            nombre=data.get("nombre"),
            telefono=data.get("telefono"),
            direccion=data.get("direccion"),
            email=data.get("email")
        )

    def update(self, data):
        self.nombre = data.get("nombre", self.nombre)
        self.telefono = data.get("telefono", self.telefono)
        self.direccion = data.get("direccion", self.direccion)
        self.email = data.get("email", self.email)
        return True

    @staticmethod
    def get_all():
        return [p.serializar() for p in ProveedorModel.db]

    @staticmethod
    def get_one(id):
        for p in ProveedorModel.db:
            if p.id == id:
                return p.serializar()
        return None

    @staticmethod
    def delete(id):
        for i, p in enumerate(ProveedorModel.db):
            if p.id == id:
                del ProveedorModel.db[i]
                return True
        return False

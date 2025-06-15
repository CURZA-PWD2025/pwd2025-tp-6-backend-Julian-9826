from app.db import db


class ProveedorModel(db.Model):
    __tablename__ = 'PROVEEDORES'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def serializar(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "email": self.email
        }

    def update(self, data):
        self.nombre = data.get("nombre", self.nombre)
        self.telefono = data.get("telefono", self.telefono)
        self.direccion = data.get("direccion", self.direccion)
        self.email = data.get("email", self.email)
        return True

    @staticmethod
    def get_all():
        return [p.serializar() for p in ProveedorModel.query.all()]

    @staticmethod
    def get_one(id):
        proveedor = ProveedorModel.query.get(id)
        return proveedor.serializar() if proveedor else None

    @staticmethod
    def delete(id):
        proveedor = ProveedorModel.query.get(id)
        if proveedor:
            db.session.delete(proveedor)
            db.session.commit()
            return True
        return False

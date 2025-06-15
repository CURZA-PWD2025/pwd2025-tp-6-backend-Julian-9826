class ArticuloModel:
    db = []  # Base de datos simulada
    id_counter = 1

    def __init__(self, descripcion, precio, stock, marca, proveedor, categorias):
        self.id = ArticuloModel.id_counter
        ArticuloModel.id_counter += 1
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca = marca
        self.proveedor = proveedor
        self.categorias = categorias

    def serializar(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "marca": self.marca,
            "proveedor": self.proveedor,
            "categorias": self.categorias
        }

    @staticmethod
    def deserializar(data):
        return ArticuloModel(
            descripcion=data.get("descripcion"),
            precio=data.get("precio"),
            stock=data.get("stock"),
            marca=data.get("marca"),
            proveedor=data.get("proveedor"),
            categorias=data.get("categorias", [])
        )

    def create(self, data):
        articulo = ArticuloModel.deserializar(data)
        ArticuloModel.db.append(articulo)
        return True

    def update(self, data):
        self.descripcion = data.get("descripcion", self.descripcion)
        self.precio = data.get("precio", self.precio)
        self.stock = data.get("stock", self.stock)
        self.marca = data.get("marca", self.marca)
        self.proveedor = data.get("proveedor", self.proveedor)
        self.categorias = data.get("categorias", self.categorias)
        return True

    @staticmethod
    def delete(id):
        for i, a in enumerate(ArticuloModel.db):
            if a.id == id:
                del ArticuloModel.db[i]
                return True
        return False

    @staticmethod
    def get_all():
        return [a.serializar() for a in ArticuloModel.db]

    @staticmethod
    def get_one(id):
        for a in ArticuloModel.db:
            if a.id == id:
                return a.serializar()
        return None

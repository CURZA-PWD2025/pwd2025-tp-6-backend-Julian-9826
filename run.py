from flask import Flask
from app.articulos.ArticuloRoutes import articulos_bp
from app.marcas.MarcaRoutes import marcas_bp
from app.categorias.CategoriaRoutes import categorias_bp
from app.proveedores.ProveedorRoutes import proveedores_bp  # 👈

app = Flask(__name__)

app.register_blueprint(articulos_bp)
app.register_blueprint(marcas_bp)
app.register_blueprint(categorias_bp)
app.register_blueprint(proveedores_bp)  # 👈

@app.route("/")
def home():
    return {"mensaje": "API TP6 funcionando correctamente"}

if __name__ == "__main__":
    app.run(debug=True)

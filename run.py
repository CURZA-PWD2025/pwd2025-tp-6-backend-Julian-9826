from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

from app.db import db  # 👈 Usamos la instancia desde db.py

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # 👈 inicializar la DB con la app

# IMPORTS DESPUÉS DE CONFIGURAR APP y DB
from app.articulos.ArticuloRoutes import articulos_bp
from app.marcas.MarcaRoutes import marcas_bp
from app.categorias.CategoriaRoutes import categorias_bp
from app.proveedores.ProveedorRoutes import proveedores_bp

app.register_blueprint(articulos_bp)
app.register_blueprint(marcas_bp)
app.register_blueprint(categorias_bp)
app.register_blueprint(proveedores_bp)

@app.route("/")
def home():
    return {"mensaje": "API TP6 funcionando correctamente"}

if __name__ == "__main__":
    app.run(debug=True)

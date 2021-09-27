from flask import Flask
# from app import db
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)


class Producto(db.Model):
    __tablename__ = 'clasificaciones'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    id_tienda = db.Column(db.Integer)
    activo = db.Column(db.Integer)

    # username = db.Column(db.String(80), unique=True, nullable=False)
    # email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, nombre, id_tienda, activo):
        self.nombre = nombre
        self.id_tienda = id_tienda
        self.activo = activo

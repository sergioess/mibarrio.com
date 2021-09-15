from flask import Flask
# from app import db
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)


class Clasificacion(db.Model):
    __tablename__ = 'clasificaciones'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))

    def __init__(self, nombre):
        self.nombre = nombre

    # def __repr__(self):
    #     return f'<clasificacion {self.nombre_clasificacion}>'

    @staticmethod
    def get_all():
        return Clasificacion.query.all()

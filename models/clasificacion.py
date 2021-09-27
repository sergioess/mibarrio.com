from flask import Flask
# from app import db
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)


class Clasificacion(db.Model):
    __tablename__ = 'categorias'

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

    # def __repr__(self):
    #     return f'<clasificacion {self.nombre_clasificacion}>'

    @ staticmethod
    def get_all():
        # return db.session.execute("SELECT * FROM clasificaciones order by nombre")
        return Clasificacion.query.filter_by(activo=1)

    @ staticmethod
    def get_by_id(id):
        return Clasificacion.query.filter_by(id=id)

    def save(self):
        if not self.id:
            db.session.add(self)

        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Clasificacion.query.filter_by(id=id).first()

    # ====== Ejecutar =============
    # user = User.get_by_email(email)

    # user = User(name=name, email=email)           Se crea el usuario, Debe tener constructor
    # user.set_password(password)
    # user.save()

    # =========  Metodos =============
    # @staticmethod
    # def get_by_email(email):
    #     return User.query.filter_by(email=email).first()

    # def set_password(self, password):
    #     self.password = generate_password_hash(password)
    # def check_password(self, password):
    #     return check_password_hash(self.password, password)
    # def save(self):
    #     if not self.id:
    #         db.session.add(self)
    #     db.session.commit()

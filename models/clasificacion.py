from flask import Flask
from flask_mongoalchemy import MongoAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = MongoAlchemy(app)


class clasificacion(db.Document):
    id = db.StringField()
    nombre_clasificacion = db.StringField()

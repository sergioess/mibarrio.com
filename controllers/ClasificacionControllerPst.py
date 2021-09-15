import sys
from flask import Flask
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify, json, make_response
from flask_mongoalchemy import MongoAlchemy
from datetime import datetime
from models.Clasificacion import Clasificacion
from bson.json_util import dumps
from flask_sqlalchemy import SQLAlchemy

import os


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


def index():

    # clasificaciones = clasificacion.query.all()

    # clasificacionesAll = db.session.query(clasificacion)
    # listaClasificaciones = []
    # print("Resultado")
    # print(clasificacionesAll)
    # for result in clasificacionesAll:
    #     listaClasificaciones.append(result.nombre)
    #     print(result.nombre)
    # print(listaClasificaciones)

    clasificaciones = Clasificacion.get_all()

    return render_template('/clasificacion/index.html', clasificaciones=clasificaciones)


def create():
    return render_template('/clasificacion/create.html')


def edit(clasificacion_id):

    return render_template('/clasificacion/edit.html')


def store():

    return "Nada"


def show(clasificacion_id):
    return render_template('/clasificacion/index.html')


def update():

    return "Nada"


def destroy(clasificacion_id):

    return redirect('/clasificacion')

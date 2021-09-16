import sys
from flask import Flask
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify, json, make_response
# from flask_mongoalchemy import MongoAlchemy
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
    # clasificaciones = Clasificacion.get_by_id(1)

    return render_template('/clasificacion/index.html', clasificaciones=clasificaciones)


def create():
    return render_template('/clasificacion/create.html')


def edit(clasificacion_id):

    return render_template('/clasificacion/edit.html')


def store():
    _nombre = request.form.get('txtNombre')
    clasifica = Clasificacion(nombre=_nombre, id_tienda=1, activo=1)
    clasifica.save()
    return redirect('/clasificacion')


def show(clasificacion_id):
    return render_template('/clasificacion/index.html')


def update():
    _id = request.form.get('txtId')
    clasificacion = Clasificacion.get_by_id(_id)
    clasificacion.nombre = request.form.get('txtNombre')
    clasificacion.save()
    return redirect('/clasificacion')


def destroy(clasificacion_id):
    _id = request.form.get('txtId')
    clasificacion = Clasificacion.get_by_id(clasificacion_id)
    clasificacion.activo = 0
    clasificacion.save()
    return redirect('/clasificacion')

import sys
from flask import Flask
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify, json, make_response
from flask_mongoalchemy import MongoAlchemy
from datetime import datetime
from models.clasificacion import db, clasificacion
from bson.json_util import dumps

import os


app = Flask(__name__)
app.config.from_object('config')

db = MongoAlchemy(app)
db.init_app(app)


def index():

    # c = Clasificacion(id="1", nombre_clasificacion="Abarrotes")
    # c.save()

    clasificaciones = clasificacion.query.all()
    # print(clasificaciones)
    # if clasificaciones:
    #     for clasifica in clasificaciones:
    #         print(clasifica.nombre_clasificacion)

    # output = []
    # for clasifica in clasificacion.query.all():
    #     output.append(
    #         {'id': clasifica.id, 'nombre': clasifica.nombre_clasificacion})
    # return jsonify({'result': output})

    # clase_producto = clasificacion.aggregate([{lookup: {from: "productos", localField: "id", foreignField: "clasificacion", as: "todos"}}])

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

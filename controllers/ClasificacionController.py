import sys
from flask import Flask
from flask import config, render_template, redirect, url_for, request, abort, flash
from flaskext.mysql import MySQL
from datetime import datetime


import os


from models.Clasificacion import Clasificacion

app = Flask(__name__)
app.config.from_object('config')

mysql = MySQL()
mysql.init_app(app)


def index():
    sql = "SELECT * FROM clasificacion;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    listaClasificaciones = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    return render_template('/clasificacion/index.html', clasificaciones=listaClasificaciones)


def create():
    return render_template('/clasificacion/create.html')


def edit(clasificacion_id):
    sql = "SELECT * FROM clasificacion WHERE id = %s;"
    datos = (clasificacion_id)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    listaEmpleados = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    return render_template('/clasificacion/edit.html', empleados=listaEmpleados)


def store():

    if request.method == 'POST':
        _nombre = request.form.get('txtNombre')

        if(_nombre == ''):
            flash('Recuerda llenar los datos de los campos')
            return redirect(url_for('empleado_bp.create'))

        sql = "INSERT INTO clasificacion (id,nombre) VALUES (NULL,%s);"
        datos = (_nombre)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, datos)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/clasificacion')
    else:
        return "Nada"


def show(clasificacion_id):
    return render_template('/clasificacion/index.html')


def update():
    if request.method == 'POST':
        _nombre = request.form.get('txtNombre')
        _id = request.form.get('txtId')

        conn = mysql.connect()
        cursor = conn.cursor()

        sql = "UPDATE clasificacion SET nombre = %s WHERE id = %s;"
        datos = (_nombre)

        cursor.execute(sql, datos)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/clasificacion')
    else:
        return "Nada"


def destroy(clasificacion_id):

    conn = mysql.connect()
    cursor = conn.cursor()

    sql = "DELETE FROM clasificacion WHERE id = %s;"
    datos = (clasificacion_id)
    cursor.execute(sql, datos)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/clasificacion')

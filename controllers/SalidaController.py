import sys
from flask import Flask
from flask import config, render_template, redirect, url_for, request, abort, flash
from flaskext.mysql import MySQL
from datetime import datetime



import os


# from models.User import User

app = Flask(__name__)
app.config.from_object('config')

mysql = MySQL()
mysql.init_app(app)



def index():
    sql="SELECT s.id, s.fecha, p.nombre_producto, s.cantidad " 
    sql+=" FROM salidas AS s  "
    sql+=" LEFT JOIN productos AS p ON (s.id_producto = p.id) "
    sql+=" ORDER BY s.fecha DESC;"

    conn= mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    listaSalidas = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()
    
    return render_template('/salida/index.html', salidas = listaSalidas)

def store():

    if request.method == 'POST':
        _id=request.form.get('txtId')
        _cantidad=request.form.get('txtCantidad')

        if(_cantidad == '' ):
            flash('Recuerda llenar los datos de los campos')
            return redirect(url_for('empleado_bp.create'))

        sql = "INSERT INTO salidas (id, id_producto,cantidad, fecha) VALUES (NULL, %s, %s, %s);"
        datos = (_id, _cantidad, datetime.now())
        conn= mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, datos)
        conn.commit()

        sql = "UPDATE productos SET cantidad = cantidad - %s WHERE id = %s;"
        datos = (_cantidad, _id)
        conn= mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, datos)
        conn.commit()

        cursor.close()
        conn.close()
        return redirect('/producto')
    else:
        return "Nada"


def destroy(salida_id):
    sql = "SELECT id_producto, cantidad FROM salidas WHERE id = %s;"
    datos = (salida_id)
    conn= mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    listaEntradas = cursor.fetchall()
    conn.commit()

    sql = "UPDATE productos SET cantidad = cantidad + %s WHERE id = %s;"
    datos = (listaEntradas[0][1] ,listaEntradas[0][0])
    conn= mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()

    sql = "DELETE FROM salidas WHERE id = %s;"
    datos = (salida_id)
    conn= mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()

    cursor.close()
    conn.close()

    return redirect('/salida')

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
    sql="SELECT p.id, p.nombre_producto, p.cantidad,p.unidad, p.imagen, p.clasificacion " 
    sql+=" , c.nombre_clasificacion, p.precio "
    sql+=" FROM productos AS p "
    sql+= " LEFT JOIN clasificacion AS c ON (p.clasificacion = c.id);"
    conn= mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    listaProductos = cursor.fetchall()

    sql= "SELECT * FROM clasificacion;"
    conn= mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    listaClasificacion = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()
    
    return render_template('/productos/index.html', productos = listaProductos, clasificaciones = listaClasificacion)
def create():
    return render_template('/producto/create.html')   

def edit(producto_id):
    sql="SELECT * FROM productos WHERE id = %s;"
    datos = (producto_id)
    conn= mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    listaproductos = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    return render_template('/productos/edit.html', productos = listaproductos)      

def store():

    if request.method == 'POST':
        _nombre=request.form.get('txtNombre')
        _clasificacion=request.form.get('txtClasificacion')
        _precio=request.form.get('txtPrecio')
        _medida=request.form.get('txtMedida')
        _foto=request.files.get('txtFoto')

        if(_nombre == '' or _clasificacion == '' or _foto == ''):
            flash('Recuerda llenar los datos de los campos')
            return redirect(url_for('producto_bp.create'))

        now=datetime.now()
        tiempo = now.strftime("%Y%H%M%S")

        if(_foto.filename != ''):
            nuevoNombreFoto = tiempo + _foto.filename
            _foto.save("uplproductos/" + nuevoNombreFoto)

        sql = "INSERT INTO productos (id, nombre_producto, precio, cantidad, clasificacion, unidad, imagen) VALUES (NULL,%s, %s, 0, %s, %s, %s);"
        datos = (_nombre, _precio, _clasificacion, _medida, nuevoNombreFoto)
        conn= mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, datos)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/producto')
    else:
        return "Nada"

    
def show(producto_id):
    return render_template('/productos/index.html')


def update():



    if request.method == 'POST':
        _nombre=request.form.get('txtNombre')
        _clasificacion=request.form.get('txtClasificacion')
        _precio=request.form.get('txtPrecio')
        _medida=request.form.get('txtMedida')
        _foto=request.files.get('txtFoto')
        _id=request.form.get('txtId')
        

        now=datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        
        conn= mysql.connect()
        cursor = conn.cursor()

        if(_foto.filename != ''):
            nuevoNombreFoto = tiempo + _foto.filename
            _foto.save("uplproductos/" + nuevoNombreFoto)

            cursor.execute("SELECT imagen FROM productos WHERE id = %s", _id)
            fila=cursor.fetchall()
            os.remove(os.path.join(app.config['CARPETA_PTOS'], fila[0][0]))

            sql = "UPDATE productos SET imagen = %s WHERE id = %s"
            datos = (nuevoNombreFoto, _id)
            cursor.execute(sql, datos)
            conn.commit()

        sql = "UPDATE productos SET nombre_producto = %s, clasificacion = %s, precio = %s, unidad = %s WHERE id = %s;"
        datos = (_nombre, _clasificacion, _precio, _medida, _id)

        cursor.execute(sql, datos)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/producto')
    else:
        return "Nada"

def destroy(producto_id):

        conn= mysql.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT imagen FROM productos WHERE id = %s", producto_id)
        fila=cursor.fetchall()
        os.remove(os.path.join(app.config['CARPETA_PTOS'], fila[0][0]))

        sql = "DELETE FROM productos WHERE id = %s;"
        datos = (producto_id)
        cursor.execute(sql, datos)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/producto')

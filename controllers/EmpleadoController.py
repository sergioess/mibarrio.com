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
    sql="SELECT * FROM empleados;"
    conn= mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    listaEmpleados = cursor.fetchall()
    # print(listaEmpleados)
    conn.commit()
    cursor.close()
    conn.close()
    
    return render_template('/empleados/index.html', empleados = listaEmpleados)
def create():
    return render_template('/empleados/create.html')   

def edit(empleado_id):
    sql="SELECT * FROM empleados WHERE id = %s;"
    datos = (empleado_id)
    conn= mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    listaEmpleados = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    return render_template('/empleados/edit.html', empleados = listaEmpleados)      

def store():
    # nombre=request.form.get("txtNombre")
    # return '''{} '''.format(nombre)


    
    if request.method == 'POST':
        _nombre=request.form.get('txtNombre')
        _correo=request.form.get('txtCorreo')
        _foto=request.files.get('txtFoto')

        if(_nombre == '' or _correo == '' or _foto == ''):
            flash('Recuerda llenar los datos de los campos')
            return redirect(url_for('empleado_bp.create'))

        now=datetime.now()
        tiempo = now.strftime("%Y%H%M%S")

        if(_foto.filename != ''):
            nuevoNombreFoto = tiempo + _foto.filename
            _foto.save("uploads/" + nuevoNombreFoto)

        # return '''
        #           <h1>The language value is: {}</h1>
        #           <h1>The framework value is: {}</h1>'''.format(_nombre, _correo)

        sql = "INSERT INTO empleados (id,nombre, correo, foto) VALUES (NULL,%s, %s, %s);"
        datos = (_nombre, _correo, nuevoNombreFoto)
        conn= mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, datos)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/empleados')
    else:
        return "Nada"

    
def show(empleado_id):
    return render_template('/empleados/index.html')


def update():



    if request.method == 'POST':
        _nombre=request.form.get('txtNombre')
        _correo=request.form.get('txtCorreo')
        _foto=request.files.get('txtFoto')
        _id=request.form.get('txtId')

        now=datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        
        conn= mysql.connect()
        cursor = conn.cursor()

        if(_foto.filename != ''):
            nuevoNombreFoto = tiempo + _foto.filename
            _foto.save("uploads/" + nuevoNombreFoto)

            cursor.execute("SELECT foto FROM empleados WHERE id = %s", _id)
            fila=cursor.fetchall()
            os.remove(os.path.join(app.config['CARPETA'], fila[0][0]))

            sql = "UPDATE empleados SET foto = %s WHERE id = %s"
            datos = (nuevoNombreFoto, _id)
            cursor.execute(sql, datos)
            conn.commit()




        sql = "UPDATE empleados SET nombre = %s, correo = %s WHERE id = %s;"
        datos = (_nombre, _correo, _id)

        cursor.execute(sql, datos)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/empleados')
    else:
        return "Nada"

def destroy(empleado_id):

        conn= mysql.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT foto FROM empleados WHERE id = %s", empleado_id)
        fila=cursor.fetchall()
        os.remove(os.path.join(app.config['CARPETA'], fila[0][0]))

        sql = "DELETE FROM empleados WHERE id = %s;"
        datos = (empleado_id)
        cursor.execute(sql, datos)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/empleados')

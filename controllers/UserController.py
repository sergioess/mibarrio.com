import sys
from flask import Flask
from flask import config, render_template, redirect, url_for, request, abort
from flaskext.mysql import MySQL


# from models.User import User

mysql = MySQL()
app2 = Flask(__name__)
app2.config['MYSQL_DATABASE_USER'] = 'root'
app2.config['MYSQL_DATABASE_PASSWORD'] = '12345678'
app2.config['MYSQL_DATABASE_DB'] = 'testpythonsistema'
app2.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app2)

def index():
    sql="insert into empleados (nombre, correo, foto) values ('Sergio4', 'sergioess24@latinmail.com', 'foto3.jpg')"
    conn= mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    
    return render_template('/user/index.html')
def store():
    return render_template('/user/index.html')
def show(userId):
    return render_template('/user/index.html')
def update(userId):
    return render_template('/user/index.html')
def delete(userId):
    return render_template('/user/index.html')
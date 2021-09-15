from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for


from routes.user_bp import user_bp
from routes.empleado_bp import empleado_bp
from routes.clasificacion_bp import clasificacion_bp
from routes.entrada_bp import entrada_bp
from routes.producto_bp import producto_bp
from routes.salida_bp import salida_bp
# from flask_mongoalchemy import MongoAlchemy

from flask import send_from_directory


app = Flask(__name__)
app.config.from_object('config')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678g@localhost:5432/mitienda'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://oxwttxarfidlxi:89e47cacfc5926776ab52a7e485b08a91bf9632736ca0843d80b6356b506f3f2@ec2-3-231-69-204.compute-1.amazonaws.com:5432/d3hr8qndm4p50h'
db = SQLAlchemy(app)


app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(empleado_bp, url_prefix='/empleados')
app.register_blueprint(clasificacion_bp, url_prefix='/clasificacion')
app.register_blueprint(entrada_bp, url_prefix='/entrada')
app.register_blueprint(producto_bp, url_prefix='/producto')
app.register_blueprint(salida_bp, url_prefix='/salida')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    # print(app.config['CARPETA'])
    return send_from_directory(app.config['CARPETA'], nombreFoto)


@app.route('/uplproductos/<nombreFoto>')
def uplproductos(nombreFoto):
    # print(app.config['CARPETA'])
    return send_from_directory(app.config['CARPETA_PTOS'], nombreFoto)


if __name__ == '__main__':
    app.run(debug=True)

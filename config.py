import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Connect to the database
SQLALCHEMY_DATABASE_URI = 'your psycopg2 URI connection'
# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False

MYSQL_DATABASE_HOST = 'localhost'
MYSQL_DATABASE_USER = 'root'
MYSQL_DATABASE_PASSWORD = '12345678'
MYSQL_DATABASE_DB = 'mitienda'

CARPETA = os.path.join('uploads')
CARPETA_PTOS = os.path.join('uplproductos')


MONGOALCHEMY_DATABASE = 'mitienda'
MONGOALCHEMY_SERVER_AUTH = False
MONGODB_HOST = 'mongodb://localhost:27017/mitienda'

import sys
from flask import Flask
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify, json, make_response
# from flask_mongoalchemy import MongoAlchemy
from datetime import datetime
from models.Produco import Produco
from bson.json_util import dumps
from flask_sqlalchemy import SQLAlchemy

import os


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)



def index():


    productos = Producto.get_all()


    return render_template('/producto/index.html', clasificaciones=clasificaciones)

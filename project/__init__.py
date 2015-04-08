# /project/__init__.py

import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('config')
db = SQLAlchemy(app)

from models import User

@app.route("/")

def hello_world():
	return "Hola Pacheco Nuevamente!"

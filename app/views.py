from flask import Flask, flash, redirect, render_template, request, session, url_for
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy

#from models import User

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

@app.route("/")
@app.route("/hello")

def hello_world():
	return "Hola Pacheco!"
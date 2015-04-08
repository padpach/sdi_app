from flask import Flask, flash, redirect, render_template, request, session, url_for
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy
#from forms import AddTaskForm, RegisterForm, LoginForm
from sqlalchemy.exc import IntegrityError

#from models import User

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from models import User

@app.route("/")

def hello_world():
	return "Hola Pacheco Nuevamente!"

def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash("necesitas loguearte primero")
			return redirect(url_for('login'))
	return wrap



# /app/models.py

from views import db
import datetime


class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(100), nullable=False)
	role = db.Column(db.String(100), default='user')

	def __init__ (self, name=None, email=None, password=None, role=None):
		self.name = name
		self.email = email
		self.password = password
		self.role = role


	def __repr__ (self):
		return'<User %r>' % (self.name)


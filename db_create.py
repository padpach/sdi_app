

# /app/db_create.py

#from config import DATABASE_PATH
from project import db
from models import User
from datetime import date



# Cremos la Base de Datos
#db.create_all()

#insertamos
#db.session.add(User("admin", "emma.pacheco@gmail.com", "adminadmin", "admin"))
#db.session.add(Task("Terminar el Tuto 3", date(2014, 03, 13), 6, 1))
#db.session.add(Task("Love Life", date(2015, 05, 05), 6, 1))

#commit
db.session.commit()
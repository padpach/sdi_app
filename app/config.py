#app/config.py

import os

#graba la ruta de la carpeta donde el script corre
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

SQLALCHEMY_DATABASE_URI = 'mysql://root:@Dedo137055@187.175.118.39/sdi_app'

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from jinja2 import Environment

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, template_folder="html_templates")
Jinja2 = Environment()
app.config["SECRET_KEY"] = "3ac0b7821f227a45f4a46ec860df39df"
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'ctf.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"


with app.app_context():
	database.create_all()
	database.session.commit()

from app import routes

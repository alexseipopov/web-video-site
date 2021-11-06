from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY']='83fb6dabd51d8e022dd9a59b4f9f3079eecb7b8f'
app.config['RECAPTCHA_PUBLIC_KEY']='6LdGYJ0cAAAAAIpekcs--P6f3t7l_9SmHt97iEMw'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

manager = LoginManager(app)

from .main import main as m
app.register_blueprint(m)

from .logreg import logreg as lr
app.register_blueprint(lr)
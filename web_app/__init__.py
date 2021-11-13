from flask import Flask
from flask_login import LoginManager
# from flask_mail import Mail
import os

directory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

app.config['SECRET_KEY']='83fb6dabd51d8e022dd9a59b4f9f3079eecb7b8f'
app.config['RECAPTCHA_PUBLIC_KEY']='6LdGYJ0cAAAAAIpekcs--P6f3t7l_9SmHt97iEMw'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

manager = LoginManager(app)
# mail = Mail(app)
# sio = SocketIO(app)

# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_USERNAME'] = 'popov2895@gmail.com'  # введите свой адрес электронной почты здесь
# app.config['MAIL_DEFAULT_SENDER'] = 'popov2895@gmail.com'  # и здесь
# app.config['MAIL_PASSWORD'] = 'Svistunov1995'



from .main import main as m
app.register_blueprint(m)

from .logreg import logreg as lr
app.register_blueprint(lr)

from .personalpage_client import pp_client
app.register_blueprint(pp_client)

from .admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint)

# @sio.on('message')
# def handle_message(message):
#     print(f'Recived message: {message}')
#     sio.emit('my_event', 'recived answer')

# from .database import db
# from .database.models import Chat
# from flask_login import current_user
# from datetime import datetime

# @sio.on('send_message')
# def recive_mess(mess):
    
#     s = Chat(user=current_user.username , message=mess, time = datetime.now())
#     db.session.add(s)
#     db.session.commit()
#     sio.emit('recived', mess)
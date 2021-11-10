from flask import Flask
from flask_login import LoginManager
from flask_socketio import SocketIO



app = Flask(__name__)

app.config['SECRET_KEY']='83fb6dabd51d8e022dd9a59b4f9f3079eecb7b8f'
app.config['RECAPTCHA_PUBLIC_KEY']='6LdGYJ0cAAAAAIpekcs--P6f3t7l_9SmHt97iEMw'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

manager = LoginManager(app)
# sio = SocketIO(app)

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
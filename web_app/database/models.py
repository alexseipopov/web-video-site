# from datetime import datetime
from flask_login import UserMixin
from . import db

class Client(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique=True, nullable = False)
    FIO = db.Column(db.String(250), nullable = False)
    phone = db.Column(db.String(250), nullable = False)
    email = db.Column(db.String(100), unique=True, nullable = False)
    password = db.Column(db.String(100), nullable = False)
    checked = db.Column(db.Boolean, default = False)

class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique=True, nullable = False)
    password = db.Column(db.String(100), nullable = False)

# class Chat(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     user = db.Column(db.String(200), nullable = False)
#     message = db.Column(db.Text, nullable = False)
#     time = db.Column(db.DateTime, default=datetime.now())

    # def __repr__(self) -> str:
    #     return type(self)

# class Personal(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(100))
#     last_name = db.Column(db.String(100))
#     fk_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
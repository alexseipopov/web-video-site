from datetime import datetime
from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique=True, nullable = False)
    phone = db.Column(db.String(250), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    reg_data = db.Column(db.DateTime, default=datetime.now())
    role = db.Column(db.Boolean)
    uniqe_hash = db.Column(db.String(50), nullable=False)


class Client(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique=True)
    last_name = db.Column(db.String(200))
    first_name = db.Column(db.String(200))
    fat = db.Column(db.String(200))
    path_file = db.Column(db.Text)
    filename = db.Column(db.Text)
    checked = db.Column(db.Boolean, default = False)
    f_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Supervision(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    f_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    username = db.Column(db.String(100), unique=True)
    FIO = db.Column(db.String(250), nullable = False, default='')
    path_file = db.Column(db.Text)
    filename = db.Column(db.Text)
    checked = db.Column(db.Boolean, default = False)


class Admin(db.Model):
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
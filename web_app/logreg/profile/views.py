from flask_login.utils import login_required, logout_user
from .. import logreg
from flask import render_template, redirect, url_for, request, flash
from ...database import db
from ...database.models import Client
from .forms import LoginForm, ClientForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from . import manager



@manager.user_loader
def load_user(user_id):
    return Client.query.get(int(user_id))

@logreg.route('/')
def index():
    return render_template('choose.html')

#registration for supervisions
# @logreg.route('/registration', methods=['POST', 'GET'])
# def registration():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         username = form.username.data
#         password = form.password.data
#         email = form.email.data
#         if Users.query.filter_by(username = username).first():
#             flash('Username exist')
#             return render_template('reg.html', title="Registration", form = form)
#         hash = generate_password_hash(password)
#         new_line = Users(username = username, email = email,  password = hash)
#         db.session.add(new_line)
#         # db.session.flush()
#         # personal = Personal(fk_user_id = new_line.id)
#         # db.session.add(personal)
#         db.session.commit()
#         return redirect(url_for('logreg.login'))
#     return render_template('reg.html', title="Registration", form = form)


#Choose a side
@logreg.route('/choose')
def reg_choose():
    return render_template('reg_choose.html')


#registration for Clients
@logreg.route('/reg', methods=['POST', 'GET'])
def reg():
    form = ClientForm()
    if form.validate_on_submit():
        phone = form.phone.data
        fio = form.last_name.data + ' ' + form.first_name.data + ' ' + form.fat_name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        user = Client(username = username, FIO = fio, phone = phone, email = email, password = generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('logreg.index'))
    return render_template('reg.html', form = form)


#login Client
@logreg.route('/login_user', methods=['POST', 'GET'])
def login_client():
    form = LoginForm()
    if form.validate_on_submit():
        client = Client.query.filter_by(username = form.username.data).first()
        if client and check_password_hash(client.password, form.password.data):
            if not client.checked:
                flash('Модерация еще не пройдена')
                return render_template('auth_client.html', form = form)
            login_user(client, form.remember.data)
            return redirect(url_for('main.index'))
        else:
            flash('Данные введены неправильно!')

    return render_template('auth_client.html', form = form)


# @logreg.route('/login', methods=['POST', 'GET'])
# def login():
    
#     form = LoginForm()
#     if form.validate_on_submit():
#         current_us = Users.query.filter_by(username = form.username.data).first()
#         if current_us and check_password_hash(current_us.password, form.password.data):
#             login_user(current_us,form.remember.data)
#             return redirect(url_for('main.index'))
#             # return "{} and {}".format(current_us.password, current_us.username)
#         flash("user not found")
#     return render_template('login.html', title = "Login", form = form)




@logreg.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
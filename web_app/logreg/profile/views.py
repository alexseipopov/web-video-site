from flask_login.utils import login_required, logout_user
from .. import logreg
from flask import render_template, redirect, url_for, request, flash
from ...database import db
from ...database.models import User, Client, Supervision
from .forms import LoginForm, RegistrationClientField, RegistrationCommonForm
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_user, current_user
from . import manager
import os
import secrets
from ... import directory



@manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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


#Common registration page
@logreg.route('/registration', methods=['POST','GET'])
def reg_choose():
    form = RegistrationCommonForm()
    if form.validate_on_submit():
        email = form.email.data
        c_u = User.query.filter_by(email=email).first()
        if c_u:
            flash('Пользователь с таким email уже существует!')
            return render_template('registration.html', form=form)
        phone = form.phone.data
        password = generate_password_hash(form.password.data)
        role = form.role.data
        if role == 'True':
            role = True
        elif role == 'False':
            role = False
        uniqe_hash = secrets.token_urlsafe(8)
        user = User(email=email, phone = phone, password=password, role = role, uniqe_hash=uniqe_hash)
        db.session.add(user)
        db.session.flush()
        if role:
            supervision = Supervision(f_id=user.id)
            db.session.add(supervision)
        else:
            client = Client(f_id = user.id)
            db.session.add(client)
        db.session.commit()
        if role:
            return redirect(url_for('main.index'))
        else:
            return redirect(url_for('logreg.reg_client', hash = uniqe_hash))
    return render_template('registration.html', form=form)


#registration for Clients
@logreg.route('/reg_<hash>', methods=['POST', 'GET'])
def reg_client(hash):
    check_user = User.query.filter_by(uniqe_hash=hash).first()
    if not check_user:
        return redirect(url_for('main.index'))
    form = RegistrationClientField()
    if form.validate_on_submit():
        print('in validation')
        last_name = form.last_name.data
        first_name = form.first_name.data
        fat = form.fat_name.data
        print(directory + '\\')
        md = directory + '\\files\\' + hash + '\sertificate'
        os.makedirs(md)

        files = []
        f = ''
        for file in form.sertificate.data:
            filename = secure_filename(file.filename)
            files.append(filename)
            file.save(md + '\\' + filename)
            f += filename + ' '
        
        
        print(files)
        print(type(files))
        
        
        user = Client.query.filter_by(f_id=check_user.id).first()
        print(user)
        user.last_name = last_name
        user.first_name = first_name
        if fat:
            user.fat = fat
        user.path_file = md
        user.filename = f
        db.session.commit()
        return redirect(url_for('logreg.index'))
    return render_template('reg.html', form = form)


#login Client
@logreg.route('/login', methods=['POST', 'GET'])
def login_client():
    form = LoginForm()
    if form.validate_on_submit():
        client = User.query.filter_by(email = form.email.data).first()
        if client and check_password_hash(client.password, form.password.data):
            if client.role:
                pass
            else:
                cl = Client.query.filter_by(f_id=client.id).first()
            if not cl.checked:
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
#         current_us = User.query.filter_by(username = form.username.data).first()
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
from flask_login.utils import login_required, logout_user
from .. import logreg
from flask import render_template, redirect, url_for, request, flash
from ...database import db
from ...database.models import Users
from .forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from . import manager



@manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@logreg.route('/registration', methods=['POST', 'GET'])
def reg():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        if Users.query.filter_by(username = username).first():
            flash('Username exist')
            return render_template('reg.html', title="Registration", form = form)
        hash = generate_password_hash(password)
        new_line = Users(username = username, email = email,  password = hash)
        db.session.add(new_line)
        # db.session.flush()
        # personal = Personal(fk_user_id = new_line.id)
        # db.session.add(personal)
        db.session.commit()
        return redirect(url_for('logreg.login'))
    return render_template('reg.html', title="Registration", form = form)


@logreg.route('/login', methods=['POST', 'GET'])
def login():
    
    form = LoginForm()
    if form.validate_on_submit():
        current_us = Users.query.filter_by(username = form.username.data).first()
        if current_us and check_password_hash(current_us.password, form.password.data):
            login_user(current_us,form.remember.data)
            return redirect(url_for('main.index'))
            # return "{} and {}".format(current_us.password, current_us.username)
        flash("user not found")
    return render_template('login.html', title = "Login", form = form)


@logreg.route('/fora')  
@login_required
def test():
    
    return Users.get_id(current_user)


@logreg.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
from flask_login.utils import login_required, logout_user
from .. import admin
from flask import render_template, redirect, url_for, request, flash
from ...database import db
from ...database.models import Admin, Client
from .forms import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user

@admin.route('/', methods=['POST', 'GET'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username = form.username.data).first()
        if admin and admin.password == form.password.data:
            login_user(admin, form.remember.data)
            return redirect(url_for('admin.page'))
        else:
            flash('Admin not found')
    return render_template('admin.html', form = form)

@admin.route('/page', methods=['POST', 'GET'])
@login_required
def page():
    clients = Client.query.order_by(Client.FIO)
    return render_template('admin_page.html', clients = clients)

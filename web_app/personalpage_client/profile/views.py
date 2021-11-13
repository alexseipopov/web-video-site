from flask_login.utils import login_required, logout_user
from .. import pp_client
from flask import render_template, redirect, url_for, request, flash
from ...database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user

@pp_client.route('/id<int:id>')
@login_required
def index(id):
    if current_user.id != id:
        pass
    return render_template('pp_client.html')
        


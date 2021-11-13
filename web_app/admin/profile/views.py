from flask_login.utils import login_required, logout_user
# from flask_mail import Message
from .. import admin
from flask import render_template, redirect, url_for, request, flash, send_from_directory
from ...database import db
from ...database.models import Admin, Client, Supervision, User
from .forms import LoginForm, VerificationForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
import smtplib
import email.message




def sum_all():
    users = User.query.order_by(User.id)
    dic = []
    
    for user in users:
        ar = {}
        if user.role:
            supervision = Supervision.query.filter_by(f_id=user.id).first()
            
        else:
            client = Client.query.filter_by(f_id=user.id).first()
            ar.setdefault('username', client.username)
            ar.setdefault('last_name', client.last_name)
            ar.setdefault('first_name', client.first_name)
            ar.setdefault('fat', client.fat)
            ar.setdefault('checked', client.checked)


        ar.setdefault('id', user.id)
        ar.setdefault('email', user.email)
        ar.setdefault('phone', user.phone)
        ar.setdefault('uniqe_hash', user.uniqe_hash)
        ar.setdefault('role', user.role)
        dic.append(ar)

    return dic



@admin.route('/', methods=['POST', 'GET'])
@login_required
def index():
    admin = Admin.query.filter_by(username = current_user.email).first()
    if not admin:
        return redirect(url_for('main.index'))
    # form = LoginForm()
    # if form.validate_on_submit():
    return redirect(url_for('admin.page'))
    #     admin = Admin.query.filter_by(username = form.username.data).first()
    #     if admin and admin.password == form.password.data:
    #         login_user(admin, form.remember.data)
    #         return redirect(url_for('admin.page'))
    #     else:
    #         flash('Admin not found')
    # return render_template('admin.html', form = form)

@admin.route('/page', methods=['POST', 'GET'])
@login_required
def page():
    admin = Admin.query.filter_by(username = current_user.email).first()
    if not admin:
        return redirect(url_for('main.index'))
    users = User.query.order_by(User.reg_data)
    count_client = Client.query.count()
    count_supervisor = Supervision.query.count()
    for client in users:
        print(client.id)
        print(type(client.id))
    print()
    return render_template('admin_page.html', clients = sum_all(), cc=count_client, cs=count_supervisor)



@admin.route('/<hash>')
def personality(hash):
    user = User.query.filter_by(uniqe_hash=hash).first()
    if user.role:
        client = Supervision.query.filter_by(f_id=user.id).first()
    else:
        client = Client.query.filter_by(f_id=user.id).first()
    files = []
    filenames =  client.filename
    print(type(filenames))
    for file in client.filename.split():
        files.append(file)
    return render_template('personality.html', client = user, about = client, files = files)

@admin.route('/<hash>/<file>')
@login_required
def dwn(hash, file):
    print(hash)
    print(file)
    user = User.query.filter_by(uniqe_hash=hash).first()
    print(user)
    if user.role:
        client = Supervision.query.filter_by(f_id=user.id).first()
    else:
        client = Client.query.filter_by(f_id=user.id).first()
    
    
    path = client.path_file
    
    
    return send_from_directory(path, file)

@admin.route('/confirm/<hash>', methods=['POST', 'GET'])
def confirm(hash):
    user = User.query.filter_by(uniqe_hash=hash).first()
    if user.role:
        client = Supervision.query.filter_by(f_id=user.id).first()
    else:
        client = Client.query.filter_by(f_id=user.id).first()
    
    client.checked = True

    # email_content = '''
    # <html>
    # <head>
    #     <title>verification video.pandabear.ru</title>
    # </head>
    # <body>
    #     Your document was checked. That's alright, you can login web-site now
    # </body> 
    # </html>
    # '''

    # msg = email.message.Message()
    # msg['Subject'] = "Verification"

    # msg['From'] = 'admin@pandabear.ru'
    # msg['To'] = 'popov2895@gmail.com'

    # password = 'AdminISP'
    # msg.add_header('Content-Type', 'text/html')
    # msg.set_payload(email_content)

    # s = smtplib.SMTP('mail.hosting.reg.ru:465')
    # s.starttls()

    # s.login(msg['From'], password)
    
    # s.sendmail(msg['From'], [msg['To']], msg.as_string())
    # s.quit()

    db.session.commit()
    return redirect(url_for('admin.page'))

@admin.route('/deconfirm/<hash>', methods=['POST', 'GET'])
def deconfirm(hash):
    user = User.query.filter_by(uniqe_hash=hash).first()
    if user.role:
        client = Supervision.query.filter_by(f_id=user.id).first()
    else:
        client = Client.query.filter_by(f_id=user.id).first()

    client.checked = False
    db.session.commit()
    return redirect(url_for('admin.page'))

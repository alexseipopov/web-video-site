from flask import Blueprint

admin = Blueprint('admin', __name__, template_folder='templates', url_prefix='/admin', static_folder='static')

from .profile import views
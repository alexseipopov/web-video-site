from flask import Blueprint

pp_client = Blueprint('pp_client', __name__, template_folder='templates', url_prefix='/client', static_folder='static')

from .profile import views
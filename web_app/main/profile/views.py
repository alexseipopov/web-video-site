from flask import render_template, send_from_directory
from .. import main
from ...database.models import Client

@main.route("/")
def index():
    return render_template('main.html')


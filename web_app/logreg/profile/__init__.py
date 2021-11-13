from ... import app
from flask_login import LoginManager

manager = LoginManager(app)

UPLOAD_FOLDER = '/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
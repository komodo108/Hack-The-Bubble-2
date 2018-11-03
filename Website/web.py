# For flask, mysql, crypto
from flask import current_app, Blueprint, render_template, send_from_directory
import os

# Setup the get blueprint
web = Blueprint('web', __name__)


@web.route('/', methods=['GET'])
def index():
    """Routes '/' to index.html"""
    return render_template('index.html', title="Hello!", render=True)


@web.route('/files/<path:filename>', methods=['GET'])
def download(filename):
    """Download the file"""
    uploads = os.path.join(current_app.root_path,
                           current_app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename)

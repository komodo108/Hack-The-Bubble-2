# For flask, mysql, crypto
from flask import Blueprint, render_template
import lounger

# Setup the get blueprint
get = Blueprint('get', __name__)


@get.route('/', methods=['GET'])
def index():
    """Routes '/' to index.html"""
    return render_template('index.html', title="Hello!", render=True)

@get.route('/loungers', methods=['GET'])
def renderLoungers():
    """Routes '/loungers' to lounger.html"""
    lounger.getBooked()


# Expected usage is that when the user clicks on a lounger and it is taken to the lounger_detail page this method will trigger the id
# will be passed into the SQL query
@get.route('/lounger_detail', methods=['GET'])
def renderDetails(id):
    """Routes '/lounger_detail to lounger_detail.html"""
    lounger.getLoungerInfo(id)
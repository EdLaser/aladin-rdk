from flask import jsonify, make_response, render_template, request, Blueprint


bp = Blueprint('routes', __name__)

@bp.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')
from flask import jsonify, make_response, render_template, request, Blueprint


bp = Blueprint('routes', __name__)

@bp.route("/", methods=['GET', 'POST'])  # type: ignore
def index():
    pass
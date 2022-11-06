from flask import render_template, request, Blueprint
from . import generate_tasks as gen

bp = Blueprint('routes', __name__)


@bp.route("/", methods=['GET', 'POST'])
def index():
    all_cases = gen.generate()
    print(all_cases)
    if request.method == 'GET':
        return render_template('index.html', li=all_cases)

    if request.method == 'POST':
        return render_template('index.html', li=all_cases)
    else:
        return render_template('index.html')

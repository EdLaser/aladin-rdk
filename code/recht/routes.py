from flask import render_template, request, Blueprint
from . import generate_tasks as gen

bp = Blueprint('routes', __name__)


@bp.route("/", methods=['GET', 'POST'])
def index():
    all_cases = gen.generate()
    ai_test = gen.call_ai()
    print(all_cases)
    if request.method == 'GET':
        return render_template('index.html', li=all_cases, test=ai_test)

    if request.method == 'POST':
        return render_template('index.html', li=all_cases, test=ai_test)
    else:
        return render_template('index.html')

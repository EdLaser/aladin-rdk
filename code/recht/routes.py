from flask import render_template, request, Blueprint
import generate_tasks as gen

bp = Blueprint('routes', __name__)


@bp.route("/", methods=['GET', 'POST'])
def index():
    all_cases = gen.generate()
    print(f"Pool_list: {all_cases['pool']}")
    if request.method == 'GET':
        return render_template('index.html', li=all_cases['li'], sol=all_cases['solution'], sum=all_cases['sum'])
    if request.method == 'POST':
        return render_template('index.html', li=all_cases['li'], sol=all_cases['solution'], sum=all_cases['sum'])
    else:
        return render_template('index.html')

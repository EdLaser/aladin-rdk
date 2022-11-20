import random

from flask import render_template, request, Blueprint
import generate_tasks as gen

bp = Blueprint('routes', __name__)


@bp.route("/", methods=['GET', 'POST'])
def index():
    diff_map = {1: random.randrange(2, 4), 2: random.randrange(5, 8), 3: random.randrange(9, 11)}

    selected_dif = request.form.get('difficutly')
    print(selected_dif)
    
    all_cases = gen.generate(diff_map.get(selected_dif))
    print(f"Pool_list: {all_cases['pool']}")
    if request.method == 'GET':
        return render_template('index.html', li=all_cases['li'], sol=all_cases['solution'], sum=all_cases['sum'])
    if request.method == 'POST':
        return render_template('index.html', li=all_cases['li'], sol=all_cases['solution'], sum=all_cases['sum'])
    else:
        return render_template('index.html')

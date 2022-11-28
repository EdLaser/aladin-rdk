import random
import logging as log

from flask import render_template, request, Blueprint
import generate_tasks as gen

bp = Blueprint('routes', __name__)


@bp.route("/", methods=['GET', 'POST'])
def index():
    diff_map = {1: random.randrange(2, 4), 2: random.randrange(5, 8), 3: random.randrange(9, 11)}

    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        selected_dif = request.form.get('difficulty')
        if selected_dif:
            all_cases = gen.generate(diff_map[int(selected_dif)])
            sentences = all_cases['sentences']
            sol = all_cases['solution']
            sum = all_cases['sum']
            cases_and_sums = all_cases['cases_and_sums']
            return render_template('index.html', sentences=sentences, sol=sol, sum=sum, cases_and_sums=cases_and_sums)
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')

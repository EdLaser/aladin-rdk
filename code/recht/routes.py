import random
import logging as log
from typing import List, Dict

from flask import render_template, request, Blueprint
from werkzeug.utils import secure_filename
import generate_tasks as gen

bp = Blueprint('routes', __name__)
ALLOWED_EXTENSIONS = {'json'}
DIFF_MAP = {1: random.randrange(2, 4), 2: random.randrange(5, 8), 3: random.randrange(9, 11)}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file(req):
    if 'file' not in request.files:
        'No file.'
    uploaded_file = req.files['file']
    if uploaded_file.filename == '':
        "No File name given."
    if uploaded_file and allowed_file(uploaded_file.filename):
        filename = secure_filename(uploaded_file.filename)  # type: ignore
        read_content = uploaded_file.read()
    else:
        return "Uploaded file not supported."
    return read_content


def return_template_with_values(generated_values, all_cases_to_choose):
    sentences = generated_values['sentences']
    sol = generated_values['solution']
    sum = generated_values['sum']
    cases_and_sums = generated_values['cases_and_sums']
    return render_template('index.html', sentences=sentences, sol=sol, sum=sum, cases_and_sums=cases_and_sums, all_cases_to_choose= all_cases_to_choose)

@bp.route("/", methods=['GET', 'POST'])
def index():
    all_cases_to_choose = gen.show_all_cases()
    
    if request.method == 'GET':
        return render_template('index.html', all_cases_to_choose= all_cases_to_choose)

    if request.method == 'POST':
        if 'file' in request.files:
            return (upload_file(request))
        else:
            # while not 'submitSolution' in request.form
            selected_dif = request.form.get('difficulty')
            needed = request.form.getlist('needed')
            
            # difficulty is not set, pick a random one
            if not selected_dif:
                # needed cases are set use them
                if needed:
                    generated_values = gen.generate(DIFF_MAP[random.randrange(1, 3)], needed)
                    return return_template_with_values(generated_values, all_cases_to_choose)
                # no needed cases ? random diff !
                else:
                    generated_values = gen.generate(DIFF_MAP[random.randrange(1, 3)])
                    return return_template_with_values(generated_values, all_cases_to_choose)
            # difficulty is set 
            else:
                # ah certain cases are needed
                if needed:
                    generated_values = gen.generate(DIFF_MAP[int(selected_dif)], needed)
                    return return_template_with_values(generated_values, all_cases_to_choose)
                # no needed cases ? Go for the set difficulty
                else:
                    generated_values = gen.generate(DIFF_MAP[int(selected_dif)])
                    return return_template_with_values(generated_values, all_cases_to_choose)
    else:
        return render_template('index.html', all_cases_to_choose= all_cases_to_choose)

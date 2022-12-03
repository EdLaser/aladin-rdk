import random
import logging as log

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
    

@bp.route("/", methods=['GET', 'POST'])
def index():
    all_cases_to_choose = gen.show_all_cases()
    
    if request.method == 'GET':
        return render_template('index.html', all_cases_to_choose= all_cases_to_choose)

    if request.method == 'POST':
        if 'file' in request.files:
            return (upload_file(request))
        if 'difficulty' in request.form:
            # while not 'submitSolution' in request.form
            selected_dif = request.form.get('difficulty')
            needed = request.form.getlist('needed')
            if not selected_dif:
                return render_template('index.html', all_cases_to_choose= all_cases_to_choose)
            else:
                if needed:
                    generated_values = gen.generate(DIFF_MAP[int(selected_dif)], needed)
                else:
                    generated_values = gen.generate(DIFF_MAP[int(selected_dif)])
                sentences = generated_values['sentences']
                sol = generated_values['solution']
                sum = generated_values['sum']
                cases_and_sums = generated_values['cases_and_sums']
                return render_template('index.html', sentences=sentences, sol=sol, sum=sum, cases_and_sums=cases_and_sums, all_cases_to_choose= all_cases_to_choose)
        else:
            return render_template('index.html' ,all_cases_to_choose= all_cases_to_choose)
    else:
        return render_template('index.html', all_cases_to_choose= all_cases_to_choose)

import random
import json
from typing import List, Dict

from flask import render_template, request, Blueprint
from library.task import Task
from werkzeug.utils import secure_filename
import generate_tasks as gen
from generator_strategie import Context, WithDifficultyAndAmount, WithDifficultyAndNeededAndAmount, Default

bp = Blueprint('routes', __name__)
ALLOWED_EXTENSIONS = {'json'}
DIFF_MAP = {1: random.randrange(2, 4), 2: random.randrange(5, 8), 3: random.randrange(9, 11)}
TASKS: List[Task] = []

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
    solutions = {}
    sentences = generated_values['sentences']
    # Dict[str, Solution]
    # TODO Remove
    sol = generated_values['solution']
    sum = generated_values['sum']
    cases_and_sums = generated_values['cases_and_sums']

    for key, value in sol.items():
        solutions[key] = value.to_dict()
    return render_template('index.html', sentences=sentences, sol=sol, solutions=solutions,  sum=sum, cases_and_sums=cases_and_sums, all_cases_to_choose= all_cases_to_choose)


def determine_strategie(parameters, context: Context):
    if parameters.get('difficulty') and parameters.get('amount'):
        if parameters.get('needed'):
            context.strategy = WithDifficultyAndNeededAndAmount() 
        else:
            context.strategy = WithDifficultyAndAmount()


def search_task(id_of_task):
    wanted_task = None
    for t in TASKS:
        if t.id == id_of_task:
            wanted_task = t
    return wanted_task


@bp.route("/get-task", methods=['GET'])
def get_tasks():
    args = request.args
    context: Context = Context(Default())
    determine_strategie(args, context)
    generated_cases = context.generate_tasks(args)
    task = Task(cases = generated_cases)
    TASKS.append(task)
    return json.dumps({"id": task.id, "sentences": [gen.build_sent(case) for case in task.cases]})


@bp.route("/select-options/<int:id_of_task>", methods=['GET'])
def get_select_options(id_of_task):
    wanted_task = search_task(id_of_task)
    if not wanted_task:
        return json.dumps({"failure": "Task was not found"})
    
    return json.dumps(gen.select_options(wanted_task.cases))

@bp.route("/solution/<int:id_of_task>", methods=['GET'])
def get_solution(id_of_task):
    zve = 0
    solutions = {}
    wanted_task = search_task(id_of_task)
    if not wanted_task:
        return json.dumps({"failure": "Task was not found"})

    for c in wanted_task.cases:
        solution = gen.build_solution(c)
        if solution.type_of_case == 'Einnahme':
            zve += solution.number
        elif solution.type_of_case == 'Ausgabe':
            zve -= solution.number
        else:
            pass
        solutions[solution.case_name] = solution.to_dict()
    solutions["zve"] = zve

    return json.dumps(solutions)


@bp.route("/", methods=['GET', 'POST'])
def index():
    all_cases_to_choose = gen.show_all_cases()
    
    if request.method == 'GET':
        return render_template('index.html', all_cases_to_choose= all_cases_to_choose)

    if request.method == 'POST':
            # while not 'submitSolution' in request.form
            selected_dif = int(request.form.get('difficulty'))
            needed = request.form.getlist('needed')
            amount = int(request.form.get('amount'))
            
            # BLOCK START
            if selected_dif == 0 and needed and amount:
                # needed cases are set use them
                generated_values = gen.generate(difficulty=DIFF_MAP[random.randrange(1, 3)], amount=amount, needed=needed)
                return return_template_with_values(generated_values, all_cases_to_choose)
            
            if selected_dif == 0 and not needed and amount:
                generated_values = gen.generate(difficulty=DIFF_MAP[random.randrange(1, 3)], amount=amount)
                return return_template_with_values(generated_values, all_cases_to_choose)
            
            if selected_dif == 0 and needed and not amount:
                pass

            if selected_dif == 0 and not needed and not amount:
                pass
            #BLOCK END

            #BLOCK START
            if selected_dif > 0 and needed and amount:
                # ah certain cases are needed
                generated_values = gen.generate(difficulty=DIFF_MAP[selected_dif], amount=amount, needed=needed)
                return return_template_with_values(generated_values, all_cases_to_choose)

            if selected_dif > 0 and not needed and amount:
                generated_values = gen.generate(DIFF_MAP[selected_dif], amount=amount,)
                return return_template_with_values(generated_values, all_cases_to_choose)

            if selected_dif > 0 and needed and not amount:
                pass

            if selected_dif > 0 and not needed and not amount:
                pass
            #BLOCK END
    else:
        return render_template('index.html', all_cases_to_choose= all_cases_to_choose)

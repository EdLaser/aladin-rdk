import random
import json
from typing import List, Dict

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from library.task import Task
from library.laws import ALL as all_laws
import generate_tasks as gen
from generator_strategie import Context, WithDifficultyAndAmount, WithDifficultyAndNeededAndAmount, Default

TASKS: List[Task] = []
origins = [
    'http://localhost:8000',
    'http://localhost:5173'
]


def determine_strategie(difficulty, amount, needed, context: Context):
    if difficulty and amount:
        if needed:
            context.strategy = WithDifficultyAndNeededAndAmount() 
        else:
            context.strategy = WithDifficultyAndAmount()


def search_task(id_of_task):
    wanted_task = None
    for t in TASKS:
        if t.id == id_of_task:
            wanted_task = t
    return wanted_task


def return_json(content):
    return JSONResponse(jsonable_encoder(content))


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['*']
)

@app.get("/get-task")
def get_tasks(difficulty: int | None = None, amount: int | None = None, needed: str | None = None):
    cases_needed = needed.split(',') if needed else []
    context: Context = Context(Default())
    determine_strategie(difficulty, amount, needed, context)
    generated_cases = context.generate_tasks(difficulty, amount, cases_needed)
    task = Task(cases = generated_cases)
    TASKS.append(task)
    return return_json({"id": task.id, "sentences": [gen.build_sent(case) for case in task.cases]})


@app.get("/select-options/{id_of_task}")
def get_select_options(id_of_task: int):
    wanted_task = search_task(id_of_task)
    if not wanted_task:
        return return_json({"failure": "Task was not found"})
    
    return return_json(gen.select_options(wanted_task.cases))

@app.get("/solution/{id_of_task}")
def get_solution(id_of_task: int):
    zve = 0
    solutions = []
    wanted_task = search_task(id_of_task)
    if not wanted_task:
        return return_json({"failure": "Task was not found"})

    for c in wanted_task.cases:
        solution = gen.build_solution(c)
        for law in all_laws:
            gen.map_law(solution, law)
        if solution.type_of_case == 'Einnahme':
            zve += solution.number
        elif solution.type_of_case == 'Ausgabe':
            zve -= solution.number
        else:
            pass
        solutions.append(solution.to_dict())
    solutions.append({"zve": zve})

    return return_json(solutions)


@app.get("/cases-to-choose")
def get_cases_to_choose():
    return return_json(list(gen.show_all_cases()))
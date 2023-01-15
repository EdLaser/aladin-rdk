from typing import List, Dict
from itertools import count
import sys
from pydantic import BaseModel
import uvicorn
from loguru import logger
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from library.task import Task
from library.nodepool.case import Case
from library.solution import Solution
from library.laws import ALL as all_laws
import generate_tasks as gen
from generator_strategie import Context, WithDifficultyAndAmount, WithDifficultyAndNeededAndAmount, Default

TASKS: List[Task] = []

origins = [
    'http://localhost:8000',
    'http://localhost:5173'
]

logger.remove()
logger.add(sys.stdout, colorize=True, format="<green>{time:HH:mm:ss}</green> | {level} | <level>{message}</level>")


class Row(BaseModel):
    id: int = 0
    select: str
    law: str
    num: int

    def __str__(self) -> str:
        return f"{self.id} {self.select} {self.law} {self.num}"


def determine_strategie(difficulty, amount, needed, context: Context):
    if difficulty and amount:
        if needed:
            context.strategy = WithDifficultyAndNeededAndAmount() 
        else:
            context.strategy = WithDifficultyAndAmount()


def solutions_with_id(solutions: List[Solution]):
    sol_and_id = {sol.case_name: sol for sol in solutions}

    return sol_and_id


def search_task(id_of_task):
    wanted_task = None
    for t in TASKS:
        if t.id == id_of_task:
            wanted_task = t
    return wanted_task


def return_json(content: Dict | List | str):
    return JSONResponse(jsonable_encoder(content))


def check_row(row: Row, correct: Solution):
    return {
        'name': correct.case_name == row.select, 
        'law': correct.law == row.law, 
        'num': correct.number == row.num
    }


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['*']
)


app.middleware("http")
async def log_request(request: Request):
    logger.debug(f"{request.method} {request.url}")
    logger.debug(f"Body: {request.body}")


@app.get("/get-task")
def get_tasks(difficulty: int | None = None, amount: int | None = None, needed: str | None = None):
    zve = 0
    cases_needed = needed.split(',') if needed else []

    context: Context = Context(Default())
    determine_strategie(difficulty, amount, needed, context)

    generated_cases = context.generate_tasks(difficulty, amount, cases_needed)
    solutions = [gen.build_solution(case) for case in generated_cases]
    for solution in solutions:
        print(solution)
        for laws in all_laws:
            gen.map_law(solution, laws)
        zve = zve + solution.number if solution.type_of_case == "Einnahme" else zve - solution.number

    task = Task(cases = generated_cases, solutions=solutions_with_id(solutions), zve=zve)
    TASKS.append(task)

    return return_json({"id": task.id, "sentences": [gen.build_sent(case) for case in task.cases]})


@app.get("/select-options/{id_of_task}")
def get_select_options(id_of_task: int):
    wanted_task = search_task(id_of_task)
    if not wanted_task:
        raise HTTPException(status_code=404, detail="Task not found.")
    
    return return_json(gen.select_options(wanted_task.cases))


@app.post("/solve/{id_of_task}")
def solve(id_of_task: int, user_rows: List[Row]):
    is_input_correct = {}
    wanted_task = search_task(id_of_task)
    if wanted_task:
        for row in user_rows:
            if row.select in wanted_task.solutions.keys():
                checked = check_row(row, wanted_task.solutions[row.select])
                wanted_task.solved[row.select] = checked
                is_input_correct[row.id] = checked
            else:
                pass
        return return_json({'given': is_input_correct, 'all_solved': wanted_task.all_solved()})
    # add zve and check if it is also solved
    if not wanted_task:
        raise HTTPException(status_code=404, detail="Task not found.")


@app.get("/solution/{id_of_task}")
def get_solution(id_of_task: int):
    wanted_task = search_task(id_of_task)
    if wanted_task:
        return return_json([solution.to_dict() for solution in wanted_task.solutions.values()])
    else:
        raise HTTPException(status_code=404, detail="Task not found.")
    


@app.get("/zve/{id_of_task}")
def get_zve(id_of_task: int):
    wanted_task = search_task(id_of_task)
    if wanted_task:
        return wanted_task.zve
    else:
        raise HTTPException(status_code=404, detail="Task not found.")


@app.get("/cases-to-choose")
def get_cases_to_choose():
    return return_json(list(gen.show_all_cases()))


@app.get("/generated-tasks")
def get_tasks_generated():
    return return_json({t.id: t.all_solved() for t in TASKS})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", log_level="debug", port=8000)
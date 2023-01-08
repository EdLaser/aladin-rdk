from typing import List, Dict
import sys
from pydantic import BaseModel
import uvicorn
from loguru import logger
from fastapi import FastAPI, HTTPException, Request
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

ERRORS = {
    404: {"code": 404, "message": "Task not found."}
}

logger.remove()
logger.add(sys.stdout, colorize=True, format="<green>{time:HH:mm:ss}</green> | {level} | <level>{message}</level>")


class Row(BaseModel):
    id: int | None = 0
    select: str | None = "test"
    law: str| None = "hallo"
    num: int | None = 0

    def __str__(self) -> str:
        return f"{self.id} {self.select} {self.law} {self.num}"


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


def check_rows(rows: List[Row], task: Task):
    pass


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
        zve = zve + solution.number if solution.type_of_case == "Einnahme" else zve - solution.number

    task = Task(cases = generated_cases, solutions=solutions, zve=zve)
    TASKS.append(task)
    
    return return_json({"id": task.id, "sentences": [gen.build_sent(case) for case in task.cases]})


@app.get("/select-options/{id_of_task}")
def get_select_options(id_of_task: int):
    wanted_task = search_task(id_of_task)
    if not wanted_task:
        raise HTTPException(status_code=404, detail="Task not found.")
    
    return return_json(gen.select_options(wanted_task.cases))

@app.post( "/solve/{id_of_task}")
def get_solution(id_of_task: int, user_rows: List[Row]):
    print(user_rows)
    
    solutions = []
    wanted_task = search_task(id_of_task)
    if not wanted_task:
        raise HTTPException(status_code=404, detail="Task not found.")

    for c in wanted_task.cases:
        solution = gen.build_solution(c)
        for law in all_laws:
            gen.map_law(solution, law)
        if solution.type_of_case == 'Einnahme':
            wanted_task.zve += solution.number
        elif solution.type_of_case == 'Ausgabe':
            wanted_task.zve -= solution.number
        else:
            pass
        solutions.append(solution.to_dict())

    return return_json(solutions)

@app.get("/zve/{id_of_task}")
def get_zve(id_of_task):
    wanted_task = search_task(id_of_task)
    if wanted_task:
        return wanted_task.zve
    else:
        return return_json(ERRORS[404])

@app.get("/cases-to-choose")
def get_cases_to_choose():
    return return_json(list(gen.show_all_cases()))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", log_level="debug", port=8000)
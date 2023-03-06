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
    """
    Represents a row in the solution table.

    Attributes:
        id (int, optional): The ID of the row. Defaults to 0.
        select (str): The selected value in the row.
        law (str): The law associated with the row.
        num (int): The numerical value associated with the row.

    Methods:
        __str__: Returns a string representation of the row.
    """
    id: int = 0
    select: str
    law: str
    num: int

    def __str__(self) -> str:
        """
        Returns a string representation of the row.

        Returns:
            str: The string representation of the row.
        """
        return f"{self.id} {self.select} {self.law} {self.num}"


def determine_strategie(difficulty, amount, needed, context: Context):
    """
    Determine the strategy based on the provided arguments and update the context object with the appropriate strategy.

    Parameters:
        difficulty (int): The difficulty level of the task.
        amount (int): The amount of tasks to generate.
        needed (bool): Whether or not the user specified a specific case to generate tasks for.
        context (Context): The context object to update with the determined strategy.
    """
    if difficulty and amount:
        if needed:
            context.strategy = WithDifficultyAndNeededAndAmount() 
        else:
            context.strategy = WithDifficultyAndAmount()


def solutions_with_id(solutions: List[Solution]):
    """
    Return a dictionary of solution objects with their case names as the key.

    Parameters:
        solutions (List[Solution]): A list of Solution objects.

    Returns:
        Dict: A dictionary of solution objects with their case names as the key.
    """
    sol_and_id = {sol.case_name: sol for sol in solutions}

    return sol_and_id


def search_task(id_of_task):
    """
    Return the task object that has the provided ID.

    Parameters:
        id_of_task (int): The ID of the task to search for.

    Returns:
        Task: The task object that has the provided ID. None if no task is found.
    """
    wanted_task = None
    for t in TASKS:
        if t.id == id_of_task:
            wanted_task = t
    return wanted_task


def return_json(content: Dict | List | str):
    """
    Return a JSON response of the provided content.

    Parameters:
        content(Dict | List | str): The content to return as a JSON response.

    Returns:
        JSONResponse: A JSON response from fastapi of the provided content.
    """
    return JSONResponse(jsonable_encoder(content))


def check_row(row: Row, correct: Solution):
    """
    Check if the provided row matches the provided correct solution.

    Parameters:
        row (Row): The row object to check.
        correct (Solution): The correct solution object to check against.

    Returns:
        Dict: A dictionary indicating whether or not the row matches the correct solution for each column.
    """
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

def get_correct_solution_value(type: str, solution: Solution):
    if type == "name":
        return solution.case_name
    elif type == "law":
        return solution.law
    elif type == "num":
        return solution.number


app.middleware("http")
async def log_request(request: Request):
    logger.debug(f"{request.method} {request.url}")
    logger.debug(f"Body: {request.body}")

@app.get("/get-task/{task_id}")
def get_certain_task(task_id: int):
    solved_with_solution = {}
    solved_variables = {}
    
    wanted_task = search_task(task_id)
    # get the task and get the solution for the already solved rows
    if not wanted_task:
        raise HTTPException(status_code=404, detail="Task not found.")
    
    # {sol_id: {'name': False, 'law': False, 'num': False} for sol_id in self.solutions.keys()}
    for case, is_solved in wanted_task.solved.items():
        # {'name': False, 'law': False, 'num': False}
        for type, solved in is_solved.items():
            if solved:
                solved_variables[type] = get_correct_solution_value(type, wanted_task.solutions[case])
            else:
                solved_variables[type] = False
            
        solved_with_solution[case] = solved_variables

    return return_json({"id": wanted_task.id, "solved": solved_with_solution, "zve": wanted_task.zve, "sentences": [gen.build_sent(case) for case in wanted_task.cases]})


@app.get("/get-task")
def get_task(difficulty: int | None = None, amount: int | None = None, needed: str | None = None):
    """
    Returns a new task.

    Parameters:
        difficulty (int | None): The difficulty of the task to generate. If None, a random difficulty will be used.
        amount (int | None): The number of cases in the task to generate. If None, a random number of cases will be used.
        needed (str | None): A comma-separated string of case names that must be included in the task. If None, all cases are eligible.

    Returns:
        A JSON response containing the id of the newly created task and a list of sentences describing the cases in the task.
    """
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
    """
    Returns the possible options for each row in a task.

    Args:
        id_of_task (int): The id of the task to get options for.

    Returns:
        A JSON response containing a list of possible options for each row in the task.
    """
    wanted_task = search_task(id_of_task)
    if not wanted_task:
        raise HTTPException(status_code=404, detail="Task not found.")
    
    return return_json(gen.select_options(wanted_task.cases))


@app.post("/solve/{id_of_task}")
def solve(id_of_task: int, user_rows: List[Row]):
    """
    Endpoint for checking user solutions to a given task. Checks each row in the user's submission and compares it to 
    the correct solution for the corresponding case. Returns a dictionary indicating whether each row is correct or not,
    as well as whether all rows have been correctly solved.

    Parameters:
        id_of_task (int): The ID of the task to solve.
        user_rows (List[Row]): A list of user submissions, each represented as a `Row` object.

    Returns:
        A JSON response with a dictionary containing two keys: "given", which maps the ID of each user submission to a 
        dictionary of three Boolean values indicating whether the user correctly identified the case name, law, and 
        number, and "all_solved", which is a Boolean indicating whether all rows have been correctly solved.

        Example return value:
        {
            "given": {
                1: {"name": True, "law": True, "num": False},
                2: {"name": True, "law": False, "num": True},
                3: {"name": False, "law": False, "num": False},
            },
            "all_solved": False
        }
    """
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
    """
    Endpoint for retrieving the correct solutions to a given task. Returns a list of dictionaries, where each dictionary 
    represents a solution to a case in the task. Each dictionary contains the case name, law, number, and type of case.

    Parameters:
        id_of_task (int): The ID of the task to retrieve solutions for.

    Returns:
        A JSON response with a list of dictionaries representing the solutions to each case in the task.

        Example return value:
        [
            {
                "case_name": "Einkauf",
                "law": "BGB § 433",
                "number": 1000,
                "type_of_case": "Ausgabe"
            },
            {
                "case_name": "Darlehen",
                "law": "BGB § 488",
                "number": 500,
                "type_of_case": "Einnahme"
            },
            ...
        ]
    """
    wanted_task = search_task(id_of_task)
    if wanted_task:
        return return_json([solution.to_dict() for solution in wanted_task.solutions.values()])
    else:
        raise HTTPException(status_code=404, detail="Task not found.")
    


@app.get("/zve/{id_of_task}")
def get_zve(id_of_task: int):
    """
    Returns the ZVE (zu versteuerndes Einkommen) of the task with the specified ID.

    Parameters:
        id_of_task (int): The ID of the task for which to get the ZVE.

    Returns:
        The ZVE of the task with the specified ID.

    Raises:
        HTTPException: If the task with the specified ID is not found.
    """
    wanted_task = search_task(id_of_task)
    if wanted_task:
        return wanted_task.zve
    else:
        raise HTTPException(status_code=404, detail="Task not found.")


@app.get("/cases-to-choose")
def get_cases_to_choose():
    """
    Returns a list of all possible cases that can be chosen in a task.

    Returns:
        A list of all possible cases that can be chosen in a task.
    """
    return return_json(list(gen.show_all_cases()))


@app.get("/generated-tasks")
def get_tasks_generated():
    """
    Returns a dictionary with the IDs of all generated tasks and their status (whether they are solved or not).

    Returns:
        A dictionary with the IDs of all generated tasks and their status (whether they are solved or not).
    """
    return return_json({t.id: t.all_solved() for t in TASKS})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", log_level="debug", port=8000)
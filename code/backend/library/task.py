from library.nodepool.case import Case
from library.solution import Solution
import itertools

class Task:
    id_generated = itertools.count()

    def __init__(self, cases: list[Case] = [], zve: int = 0, solutions: dict[int, Solution] = {}) -> None:
        self.id = next(Task.id_generated)
        self.cases: list[Case] = cases
        self.solutions: dict[int, Solution] = solutions
        self.zve = zve
        self.solved = {sol_id: False for sol_id in self.solutions.keys()}

    def to_dict(self):
        return {"id": self.id, "case": [case.to_dict() for case in self.cases], "solved": self.solved}
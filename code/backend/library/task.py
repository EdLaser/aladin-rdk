from library.nodepool.case import Case
from library.solution import Solution
import itertools

class Task:
    id_generated = itertools.count()

    def __init__(self, cases: list[Case] = [], zve: int = 0, solutions: list[Solution] = [], solved: bool=False) -> None:
        self.id = next(Task.id_generated)
        self.cases: list[Case] = cases
        self.solutions = solutions
        self.zve = zve
        self.solved = solved

    def to_dict(self):
        return {"id": self.id, "cases": [case.to_dict() for case in self.cases], "solved": self.solved}
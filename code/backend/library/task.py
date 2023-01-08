from library.nodepool.case import Case
from library.solution import Solution
import itertools

class Task:
    id_generated = itertools.count()

    def __init__(self, cases: dict[int, Case] = {}, zve: int = 0, solutions: list[Solution] = []) -> None:
        self.id = next(Task.id_generated)
        self.cases: dict[int, Case] = cases
        self.solutions = solutions
        self.zve = zve
        self.solved = {case_id: False for case_id in self.cases.keys()}

    def to_dict(self):
        return {"id": self.id, "cases": [case.to_dict() for case in self.cases.values()], "solved": self.solved}
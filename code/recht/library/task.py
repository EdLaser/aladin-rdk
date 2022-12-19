from library.nodepool.case import Case
import itertools

class Task:
    id_generated = itertools.count()

    def __init__(self, cases: list[Case]=[], solved: bool=False) -> None:
        self.id = next(Task.id_generated)
        self.cases: list[Case] = cases
        self.solved = solved

    def to_dict(self):
        return {"id": self.id, "cases": [case.to_dict() for case in self.cases], "solved": self.solved}
from abc import ABC, abstractmethod
import generate_tasks as gen
from random import randrange
from library.nodepool.case import Case

class GeneratorStrategie(ABC):
    @abstractmethod
    def generate(self, difficulty: int | None, amount: int | None, needed: list[str] | None) -> list[Case]:
        pass

class WithDifficultyAndNeededAndAmount(GeneratorStrategie):
    def generate(self, difficulty: int, amount: int, needed: list[str]) -> list[Case]:
        return gen.generate(difficulty=difficulty, amount=amount, needed=needed)

class WithDifficultyAndAmount(GeneratorStrategie):
    def generate(self, difficulty: int, amount: int, needed: list[str]) -> list[Case]:
        return gen.generate(difficulty=difficulty, amount=amount)

class Default(GeneratorStrategie):
    def generate(self, difficulty, amount, needed) -> list[Case]:
        return gen.generate()

class Context:
    def __init__(self, strategy: GeneratorStrategie):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: GeneratorStrategie):
        self._strategy = strategy

    # The Context delegates the execution of the algorithm to the strategy object.
    def generate_tasks(self, difficulty: int | None, amount: int | None, needed: list[str] | None) -> list[Case]:
        return self._strategy.generate(difficulty, amount, needed)

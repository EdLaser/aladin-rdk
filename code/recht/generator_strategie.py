from abc import ABC, abstractmethod
import generate_tasks as gen
from random import randrange
from library.nodepool.case import Case

class GeneratorStrategie(ABC):
    DIFF_MAP = {1: randrange(2, 4), 2: randrange(5, 8), 3: randrange(9, 11)}
    @abstractmethod
    def generate(self, parameters) -> list[Case]:
        pass

class WithDifficultyAndNeededAndAmount(GeneratorStrategie):
    def generate(self, parameters) -> list[Case]:
        return gen.generate(difficulty=self.DIFF_MAP[int(parameters.get('difficulty'))], amount=int(parameters.get('amount')), needed=parameters.get('needed'))

class WithDifficultyAndAmount(GeneratorStrategie):
    def generate(self, parameters) -> list[Case]:
        return gen.generate(difficulty=self.DIFF_MAP[int(parameters.get('difficulty'))], amount=int(parameters.get('amount')))

class Default(GeneratorStrategie):
    def generate(self, parameters) -> list[Case]:
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
    def generate_tasks(self, parameters) -> list[Case]:
        return self._strategy.generate(parameters)

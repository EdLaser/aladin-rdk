from abc import ABC, abstractmethod
import generate_tasks as gen
from library.nodepool.case import Case

class GeneratorStrategie(ABC):
    @abstractmethod
    def generate(self) -> list[Case]:
        pass

class WithDifficultyAndNeededAndAmount(GeneratorStrategie):
    def generate(self, parameters) -> list[Case]:
        return gen.generate(difficulty=parameters.get('difficulty'), amount=parameters.get('amount'), needed=parameters.get('needed'))

class WithDifficultyAndAmount(GeneratorStrategie):
    def generate(self, parameters) -> list[Case]:
        return gen.generate(difficulty=parameters.get('difficulty'), amount=parameters.get('amount'))

class Default(GeneratorStrategie):
    def generate(self) -> list[Case]:
        return gen.generate()

class Context:
    def __init__(self, strategy: GeneratorStrategie):
        self._strategy = strategy

    def set_strategy(self, strategy: GeneratorStrategie):
        self._strategy = strategy

    # The Context delegates the execution of the algorithm to the strategy object.
    def generate_tasks(self) -> list[Case]:
        self._strategy.generate()

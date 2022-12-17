from abc import ABC, abstractmethod
import generate_tasks as gen

class GeneratorStrategie(ABC):
    @abstractmethod
    def generate(self):
        pass

class WithDifficultyAndNeededAndAmount(GeneratorStrategie):
    def generate(self, parameters):
        return gen.generate(difficulty=parameters.get('difficulty'), amount=parameters.get('amount'), needed=parameters.get('needed'))

class WithDifficultyAndAmount(GeneratorStrategie):
    def generate(self, parameters):
        return gen.generate(difficulty=parameters.get('difficulty'), amount=parameters.get('amount'))

class Default(GeneratorStrategie):
    def generate(self):
        return gen.generate()

class Context:
    def __init__(self, strategy: GeneratorStrategie):
        self._strategy = strategy

    def set_strategy(self, strategy: GeneratorStrategie):
        self._strategy = strategy

    # The Context delegates the execution of the algorithm to the strategy object.
    def generate_tasks(self):
        self._strategy.generate()

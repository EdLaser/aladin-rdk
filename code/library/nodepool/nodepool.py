import random
from library.nodepool.case import Case

class NodePool:
    def __init__(self, name: str) -> None:
        self.name = name
        self.nodes = []

    def show_nodes(self) -> list[Case]:
        return self.nodes

    def add_node(self, node: Case) -> list[Case]:
        self.nodes.append(node)
        return self.show_nodes()

    def remove_node(self, node: Case) -> list[Case]:
        self.nodes.remove(node)
        return self.show_nodes()

    def pick_random_node(self) -> Case:
        return random.choice(self.nodes)
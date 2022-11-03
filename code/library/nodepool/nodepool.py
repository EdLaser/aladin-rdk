import random

class NodePool:
    def __init__(self, name) -> None:
        self.name = name
        self.nodes = []

    def show_nodes(self) -> list:
        return self.nodes

    def add_node(self, node) -> list:
        self.nodes += node
        return self.show_nodes()

    def remove_node(self, node) -> list:
        self.nodes.remove(node)
        return self.show_nodes()

    def pick_random_node(self):
        return random.choice(self.nodes)
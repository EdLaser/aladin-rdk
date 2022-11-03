import random
from library.nodepool.case import Case

class NodePool:
    def __init__(self, name: str) -> None:
        self.name = name
        self.nodes = []

    def __iter__(self):
        return iter(self.nodes)

    def show_nodes(self) -> list[Case]:
        '''Show all nodes of the pool.'''
        return self.nodes

    def add_node(self, node: Case) -> list[Case]:
        '''Add a node to the pool.'''
        self.nodes.append(node)
        return self.show_nodes()

    def remove_node(self, node: Case) -> list[Case]:
        '''Remove a node from the pool.'''
        self.nodes.remove(node)
        return self.show_nodes()

    def pick_random_node(self) -> Case:
        '''Pick a random node out of the pool.'''
        return random.choice(self.nodes)
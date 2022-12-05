import random
from typing import List, Dict
from library.nodepool.case import Case

class NodePool:
    def __init__(self, name: str) -> None:
        self.name = name
        self.nodes: List[Case] = []

    def __iter__(self):
        return iter(self.nodes)

    def show_nodes(self) -> List[str]:
        '''Show all nodes of the pool.'''
        nodes_as_string = []
        for c in self.nodes:
            nodes_as_string.append(str(c))
        return nodes_as_string
        
    def pick_node(self, wanted_case: str):
        for case in self.nodes:
            if case.name == wanted_case:
                return case
            else:
                pass

    def add_node(self, node: Case) -> List[str]:
        '''Add a node to the pool.'''
        self.nodes.append(node)
        return self.show_nodes()

    def remove_node(self, node: Case) -> List[str]:
        '''Remove a node from the pool.'''
        self.nodes.remove(node)
        return self.show_nodes()

    def pick_random_node(self) -> Case:
        '''Pick a random node out of the pool.'''
        return random.choice(self.nodes)
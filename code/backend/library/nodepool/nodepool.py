import random
from typing import List, Dict
from library.nodepool.case import Case

class NodePool:
    """
    A class that represents a pool of nodes.

    Parameters:
        name (str): The name of the node pool.
        nodes (List[Case]): A list of Case objects representing the nodes in the pool.

    Methods:
        __iter__(): Returns an iterator over the nodes in the pool.
        show_nodes(): Returns a list of strings representing the nodes in the pool.
        pick_node(wanted_case: str): Returns the Case object corresponding to the specified case name, or None if not found.
        add_node(node: Case): Adds a Case object representing a node to the pool.
        remove_node(node: Case): Removes a Case object representing a node from the pool.
        pick_random_node(): Returns a random Case object representing a node from the pool.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a NodePool object with the specified name.

        Parameters:
            name (str): The name of the node pool.
        """
        self.name = name
        self.nodes: List[Case] = []

    def __iter__(self):
        """
        Returns an iterator over the nodes in the pool.
        """
        return iter(self.nodes)

    def show_nodes(self) -> List[str]:
        """
        Returns a list of strings representing the nodes in the pool.

        Returns:
            List[str]: A list of strings representing the nodes in the pool.
        """
        nodes_as_string = []
        for c in self.nodes:
            nodes_as_string.append(str(c))
        return nodes_as_string
        
    def pick_node(self, wanted_case: str):
        """
        Returns the Case object corresponding to the specified case name, or None if not found.

        Parameters:
            wanted_case (str): The name of the case to find.

        Returns:
            Case: The Case object corresponding to the specified case name, or None if not found.
        """
        for case in self.nodes:
            if case.name == wanted_case:
                return case
            else:
                pass

    def add_node(self, node: Case) -> List[str]:
        """
        Adds a Case object representing a node to the pool.

        Parameters:
            node (Case): The Case object representing the node to add to the pool.

        Returns:
            List[str]: A list of strings representing the nodes in the pool after the addition.
        """
        self.nodes.append(node)
        return self.show_nodes()

    def remove_node(self, node: Case) -> List[str]:
        """
        Removes a Case object representing a node from the pool.

        Parameters:
            node (Case): The Case object representing the node to remove from the pool.

        Returns:
            List[str]: A list of strings representing the nodes in the pool after the removal.
        """
        self.nodes.remove(node)
        return self.show_nodes()

    def pick_random_node(self) -> Case:
        """
        Returns a random Case object representing a node from the pool.

        Returns:
            Case: A random Case object representing a node from the pool.
        """
        return random.choice(self.nodes)
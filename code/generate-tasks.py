import random
import string
import pprint
import networkx as nx
import matplotlib.pyplot as plt
from dag.graph import Graph
from dag.vertex import Vertex
from library import earnings
from library import numbers
from library import dependencys


def setup_graph():
    g = nx.DiGraph()
    g.add_node("start", value="", depth=0)
    combos = dependencys.map_parts()
    
    for earning_key, earning_type in combos.items():
        g.add_node(node_for_adding=earning_key, value=earning_type, depth=1)
        g.add_edge("start", earning_key)
        print(earning_key)
        print(earning_type)
        
        for key, phrase in earning_type.items():
            g.add_node(node_for_adding= f"{earning_key}.{key}", value=phrase, depth=2)
            g.add_edge(earning_key, f"{earning_key}.{key}")

    print("\n")
    
    for elem in g:
        print(f"Node: {elem}\n---\tValue: {g.nodes[elem]}\n")   
    
    return g

def traverse(difficculty: int, graph):
    # Traversiere immer wieder mit einer zufälligen Kombination
    for i in range(difficculty):
        successors = graph.successors()

if __name__ == '__main__':
    # char = random.choice(string.ascii_letters).upper()
    g = setup_graph()
    pprint.pprint(dependencys.map_parts())
   
    pos = nx.spring_layout(g)
    plt.figure()
    nx.draw_planar(g, arrows=True)
    plt.savefig("graph.png", format="PNG")
    plt.clf()

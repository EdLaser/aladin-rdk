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
    
    for key_comb, value_comb in combos.items():
        g.add_node(node_for_adding=key_comb, value=value_comb, depth=1)
        g.add_edge("start", key_comb)
        
        for earning_type, parts_earning in value_comb.items():
            g.add_node(node_for_adding= f"{key_comb}.{earning_type}", value=parts_earning, depth=2)
            g.add_edge(key_comb, f"{key_comb}.{earning_type}")
        
            for phrase, value in parts_earning.items():
                g.add_node(node_for_adding=f"{key_comb}.{earning_type}.{phrase}", value=value, depth=3)
                g.add_edge(f"{key_comb}.{earning_type}", f"{key_comb}.{earning_type}.{phrase}")

    print("\n")
    
    for elem in g:
        print(f"Node: {elem}\n---\tValue: {g.nodes[elem]}\n")
    pos = nx.spring_layout(g)
    plt.figure()
    nx.draw_planar(g, arrows=True)
    plt.savefig("graph.png", format="PNG")
    plt.clf()

def traverse(dicciculty: int, graph):
    for node in graph:
        pass

if __name__ == '__main__':
    # char = random.choice(string.ascii_letters).upper()
    setup_graph()
    pprint.pprint(dependencys.map_parts())

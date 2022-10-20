import random
import string
import networkx as nx
import matplotlib.pyplot as plt
from dag.graph import Graph
from dag.vertex import Vertex
from library import earnings
from library import numbers
from library import dependencys


def setup_graph():
    g = nx.DiGraph()
    g.add_node("start", value="")

    for key_comb, value_comb in dependencys.COMBINATIONS.items():
        g.add_node(node_for_adding=key_comb, value=value_comb)
        g.add_edge("start", key_comb)
        
        for key_earn, value_earn in earnings.ALL.items():
            g.add_node(node_for_adding= f"{key_comb}.{key_earn}", value=value_earn, nodetype=key_earn)
            g.add_edge(key_comb, f"{key_comb}.{key_earn}")
        
            for value_num in numbers.ALL.items():
                g.add_node(node_for_adding=f"{key_comb}.{key_earn}.{value_num}", value=value_num)
                g.add_edge(f"{key_comb}.{key_earn}", f"{key_comb}.{key_earn}.{value_num}")

    print("\n")
    
    print(g.nodes)
    print(g.edges)
    pos = nx.spring_layout(g)
    plt.figure()
    nx.draw_planar(g, arrows=True)
    plt.savefig("graph.png", format="PNG")
    plt.clf()


if __name__ == '__main__':
    char = random.choice(string.ascii_letters).upper()
    setup_graph()

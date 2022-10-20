import random
import string
from dag.graph import Graph
from dag.vertex import Vertex
from library import earnings
from library import numbers
from library import dependencys


def setup_graph():
    g = Graph()
    g.add_vertex("start", "")

    for key_comb, value_comb in dependencys.COMBINATIONS.items():
        print(g.add_vertex(key_comb, value_comb))
        g.add_edge("start", key_comb)

        for key_earn, value_earn in earnings.ALL.items():
            print(g.add_vertex(key_earn, value_earn))
            g.add_edge(key_comb, key_earn)

    print("\n")
    for vert in g:
        print(vert)


if __name__ == '__main__':
    char = random.choice(string.ascii_letters).upper()
    setup_graph()

import string
import pprint
import networkx as nx
import matplotlib.pyplot as plt
from library import dependencys


def setup_graph():
    g = nx.DiGraph()
    g.add_node("start", value="", depth=0)
    combos = dependencys.map_parts()
    pprint.pprint(combos)
    for earning_key, earning_type in combos.items():
        g.add_node(node_for_adding=earning_key, value=earning_type, depth=1)
        g.add_edge("start", earning_key)

        # for key, phrase in earning_type.items():
        #     g.add_node(
        #         node_for_adding=f"{earning_key}.{key}", value=phrase, depth=2)
        #     g.add_edge(earning_key, f"{earning_key}.{key}")

    print("\n")

    # for elem in g:
    #     print(f"Node: {elem}\n---\tValue: {g.nodes[elem]}\n")

    return g


def traverse(difficculty: int, graph):
    # Traversiere immer wieder mit einer zufälligen Kombination
    pprint.pprint(list(graph.nodes(data='value')))
    for i in range(difficculty):
        pass


if __name__ == '__main__':
    # char = random.choice(string.ascii_letters).upper()
    g = setup_graph()
    traverse(5, g)
    pos = nx.spring_layout(g)
    plt.figure()
    nx.draw_planar(g, arrows=True)
    plt.savefig("graph.png", format="PNG")
    plt.clf()

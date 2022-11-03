from platform import node
import random
import pprint
import networkx as nx
import matplotlib.pyplot as plt
from library import dependencys
from library import variations as var

# Lets create a node pool with all possible cases
# According to difficulty we pull a node out of the pool and get the associated case
# Then we either put it back in the pool or take it out to make more easier tasks


def setup_graph():
    g = nx.DiGraph()
    g.add_node("start", value="", depth=0)
    combos = dependencys.map_parts()
    # pprint.pprint(combos)
    for earning_key, earning_type in combos.items():
        g.add_node(node_for_adding=earning_key, value=earning_type, depth=1)
        g.add_edge("start", earning_key)

        # for key, phrase in earning_type.items():
        #     g.add_node(
        #         node_for_adding=f"{earning_key}.{key}", value=phrase, depth=2)
        #     g.add_edge(earning_key, f"{earning_key}.{key}")

    # for elem in g:
    #     print(f"Node: {elem}\n---\tValue: {g.nodes[elem]}\n")

    return g


def build_sent(key, parts: dict):
    if isinstance(parts, dict):
        variations = var.build_variatons(key, parts)
        if variations:
            print(random.choice(variations))


def traverse(difficculty: int, graph):
    # Traversiere immer wieder mit einer zufälligen Kombination
    nodes = list(graph.nodes(data='value'))
    node_values = random.sample(nodes, difficculty)
    print("\n")
    for i in node_values:
        build_sent(i[0], i[1])


if __name__ == '__main__':
    # char = random.choice(string.ascii_letters).upper()
    g = setup_graph()
    traverse(5, g)
    pos = nx.spring_layout(g)
    plt.figure()
    nx.draw_planar(g, arrows=True)
    plt.savefig("graph.png", format="PNG")
    plt.clf()

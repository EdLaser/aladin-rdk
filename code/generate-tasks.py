import random
import pprint
from library import dependencys
from library import variations as var
from library.nodepool.nodepool import NodePool
from library.nodepool.case import Case

# Lets create a node pool with all possible cases
# According to difficulty we pull a node out of the pool and get the associated case
# Then we either put it back in the pool or take it out to make more easier tasks


def setup_pool(name, cases) -> NodePool:
    pool = NodePool(name)
    for c in cases:
        pool.add_node(c)

    return pool


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
    pass

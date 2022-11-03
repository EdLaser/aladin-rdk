import random

from library import dependencys as dep
from library import sentenceparts as sen
from library import variations as var
from library import numbers as num
from library.nodepool.nodepool import NodePool
from library.nodepool.case import Case

# Lets create a node pool with all possible cases
# According to difficulty we pull a node out of the pool and get the associated case
# Then we either put it back in the pool or take it out to make more easier tasks


def setup_pool(name: str, cases: list[Case]) -> NodePool:
    pool = NodePool(name)
    for c in cases:
        pool.add_node(c)

    return pool


def build_sent(case: Case):
    '''
    Build a sentence for the given case.

    Parameters:
        case(Case): The case to build the sentence for.
    '''
    variation = var.build_variaton(case)
    if variation:
        print(variation)


def traverse(difficculty: int, nodepool: NodePool):
    '''
    Pick a node of the pool the given ammount of times.

    Parameters:
        difficulty(int): Ammount of pickings from the nodepool.
        nodepool(NodePool): The nodepool to pick the nodes from.
    '''
    # Traversiere immer wieder mit einer zufälligen Kombination
    for x in range(difficculty):
        build_sent(nodepool.pick_random_node())


if __name__ == '__main__':
    # char = random.choice(string.ascii_letters).upper()
    all_cases = dep.generate_all_cases(formulation_dict=sen.EARNINGS, verbs=sen.VERBS, numbers=num.ALL)
    
    pool = setup_pool('test_pool', all_cases)
    
    for c in pool:
        print(c)

    traverse(3, pool)

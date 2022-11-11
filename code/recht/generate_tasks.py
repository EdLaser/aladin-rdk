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


def add_all(pool: NodePool, cases: list[Case]) -> None:
    for c in cases:
        pool.add_node(c)



def build_sent(case: Case):
    '''
    Build a sentence for the given case.

    Parameters:
        case(Case): The case to build the sentence for.
    '''
    variation = var.build_variaton(case)
    if variation:
        print(f"Generated: {variation}")
        return variation
    else:
        print(f"Generated: {variation}")
        return "Failure in Generation."



def traverse(difficculty: int, nodepool: NodePool):
    '''
    Pick a node of the pool the given ammount of times.

    Parameters:
        difficulty(int): Ammount of pickings from the nodepool.
        nodepool(NodePool): The nodepool to pick the nodes from.
    '''
    # Traversiere immer wieder mit einer zufälligen Kombination
    elements = []
    for x in range(difficculty):
        random_case = nodepool.pick_random_node()
        elements.append(build_sent(random_case))
        nodepool.remove_node(random_case)
    return elements


def generate() -> dict:
    # char = random.choice(string.ascii_letters).upper()
    earning_cases = dep.generate_all_earning_cases(
        formulation_dict=sen.EARNINGS, verbs=sen.VERBS, numbers=num.ALL)
    spending_cases = dep.generate_all_spending_cases(
        formulation_dict=sen.SPENDINGS, verbs=sen.VERBS, numbers=num.ALL, object=earning_cases[0].subject)

    pool = setup_pool('test_pool', earning_cases)
    add_all(pool, spending_cases)

    li = traverse(4, pool)

    pool_list = []
    for c in pool.nodes:
        pool_list.append(str(c))
    print(f"Liste: {li}")
    
    return {'li': li, 'pool': pool_list}


if __name__ == '__main__':
    # for e in var.test(""):
    #     print(e)
    generate()
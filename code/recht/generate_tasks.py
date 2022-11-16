import random
from typing import List, Dict
from library import dependencys as dep
from library import sentenceparts as sen
from library import variations as var
from library import numbers as num
from library import laws as law
from library.solution import Solution
from library.nodepool.nodepool import NodePool
from library.nodepool.case import Case

# Lets create a node pool with all possible cases
# According to difficulty we pull a node out of the pool and get the associated case
# Then we either put it back in the pool or take it out to make more easier tasks


def setup_pool(name: str, cases: List[Case]) -> NodePool:
    pool = NodePool(name)
    for c in cases:
        pool.add_node(c)

    return pool


def add_all(pool: NodePool, cases: List[Case]) -> None:
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


def map_laws(sol: Solution, rand_case: Case) -> Solution:
    sol.case_name = rand_case.name
    for key_nst, val_nst in law.NICHT_SELBSTSTÄNDIG.items():
        if rand_case.name in val_nst:
            sol.law = key_nst
    for key_ver, val_ver in law.VERMIETUNG.items():
        if rand_case.name in val_ver:
            sol.law = key_ver
    for key_ktv, val_ktv in law.KAPITALVERMOEGEN.items():
        if rand_case.name in val_ktv:
            sol.law = key_ktv
    for key_wk, val_wk in law.WERBUNGSKOSTEN.items():
        if rand_case.name in val_wk:
            sol.law = key_wk
    sol.number = rand_case.number
    return sol

def traverse(difficculty: int, nodepool: NodePool, sol:Dict):
    '''
    Pick a node of the pool the given ammount of times.

    Parameters:
        difficulty(int): Ammount of pickings from the nodepool.
        nodepool(NodePool): The nodepool to pick the nodes from.
        sol(dict): Dictionary of the Solutions
    '''
    # Traversiere immer wieder mit einer zufälligen Kombination
    elements = []
    for x in range(difficculty):
        so = Solution()
        random_case = nodepool.pick_random_node()
        elements.append(build_sent(random_case))
        sol[random_case.name] = map_laws(so, random_case)
        nodepool.remove_node(random_case)
    return elements


def generate() -> Dict:
    solution = {}
    pool_list = []
    sum_of_solution = 0

    earning_cases = dep.generate_all_earning_cases(
        formulation_dict=sen.EARNINGS, verbs=sen.VERBS, numbers=num.ALL)
    spending_cases = dep.generate_all_spending_cases(
        formulation_dict=sen.SPENDINGS, verbs=sen.VERBS, numbers=num.ALL, object=earning_cases[0].subject)

    pool = setup_pool('test_pool', earning_cases)
    add_all(pool, spending_cases)

    li = traverse(4, pool, solution)

    for c in pool.nodes:
        pool_list.append(str(c))
    print(f"Liste: {li}")
    for s, o in solution.items():
        print(f"Key: {s} Value (Solution): {o}")
        sum_of_solution += o.number
    
    return {'li': li, 'pool': pool_list, 'solution': solution, 'sum': sum_of_solution}


if __name__ == '__main__':
    # for e in var.test(""):
    #     print(e)
    generate()
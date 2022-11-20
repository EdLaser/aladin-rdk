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
    """
    Build a sentence for the given case.

    Parameters:
        case(Case): The case to build the sentence for.
    """
    variation = var.build_variaton(case)
    if variation:
        print(f"Generated: {variation}")
        return variation
    else:
        print(f"Generated: {variation}")
        return "Failure in Generation."


def calculate_zve(solutions: Dict[str, Solution]) -> int:
    zve = 0
    for sol in solutions.values():
        if sol.type_of_case == 'Einnahme':
            zve += sol.number
        elif sol.type_of_case == 'Ausagbe':
            zve -= sol.number
        else:
            pass
    return zve


def map_laws(sol: Solution, rand_case: Case) -> Solution:
    sol.case_name = rand_case.name
    if 'WK' in sol.case_name or 'Abschreibung' in sol.case_name:
        sol.type_of_case = 'Ausgabe'
    else:
        sol.type_of_case = 'Einnahme'

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


def traverse(difficulty: int, nodepool: NodePool, sol: Dict):
    """
    Pick a node of the pool the given ammount of times.

    Parameters:
        difficulty(int): Ammount of pickings from the nodepool.
        nodepool(NodePool): The nodepool to pick the nodes from.
        sol(dict): Dictionary of the Solutions
    """
    # Traversiere immer wieder mit einer zufälligen Kombination
    elements = []
    for x in range(difficulty):
        so = Solution()
        random_case = nodepool.pick_random_node()
        elements.append(build_sent(random_case))
        sol[random_case.name] = map_laws(so, random_case)
        nodepool.remove_node(random_case)
    return elements


def generate() -> Dict:
    solutions = {}
    pool_list = []

    earning_cases = dep.generate_all_earning_cases(
        formulation_dict=sen.EARNINGS, verbs=sen.VERBS, numbers=num.ALL)
    spending_cases = dep.generate_all_spending_cases(
        formulation_dict=sen.SPENDINGS, verbs=sen.VERBS, numbers=num.ALL, object=earning_cases[0].subject)

    pool = setup_pool('test_pool', earning_cases)
    add_all(pool, spending_cases)

    li = traverse(4, pool, solutions)

    for c in pool.nodes:
        pool_list.append(str(c))
    print(f"Liste: {li}")
    for s, o in solutions.items():
        print(f"Key: {s} Value (Solution): {o}")

    zve = calculate_zve(solutions)

    return {'li': li, 'pool': pool_list, 'solution': solutions, 'sum': zve}


if __name__ == '__main__':
    # for e in var.test(""):
    #     print(e)
    generate()

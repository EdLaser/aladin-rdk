import json
from typing import List, Dict
from library import dependencies as dep
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

def read_config(file_name: str):
    with open(file_name, 'r') as f:
        content = f.read()
    try:
        config_dict = json.loads(content)
        return config_dict
    finally:
        return "Parsing config failed."


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
        return variation
    else:
        return "Failure in Generation."


def calculate_zve(solutions: Dict[str, Solution]) -> int:
    zve = 0
    for sol in solutions.values():
        if sol.type_of_case == 'Einnahme':
            zve += sol.number
        elif sol.type_of_case == 'Ausgabe':
            zve -= sol.number
        else:
            pass
    return zve


def map_laws(solutions: Dict[str, Solution], config: Dict[str, List[str]]):
    for given_law, list_of_dep_cases in config.items():
        for solution_name, sol in solutions.items():
            if solution_name in list_of_dep_cases:
                sol.law = given_law
            else:
                pass


def pick(difficulty: int, nodepool: NodePool, sol: Dict[str, Solution]) -> List[str]:
    """
    Pick a node of the pool the given ammount of times.

    Parameters:
        difficulty(int): Ammount of pickings from the nodepool.
        nodepool(NodePool): The nodepool to pick the nodes from.
        sol(dict): Dictionary of the Solutions
    """
    # Traversiere immer wieder mit einer zufälligen Kombination
    sentences = []
    for x in range(difficulty):
        random_case = nodepool.pick_random_node()
        sentences.append(build_sent(random_case))
        if 'WK' in random_case.name or 'Abschreibung' in random_case.name:
            sol[random_case.name] = Solution(case_name=random_case.name, number=random_case.number,
                                             type_of_case='Ausgabe')
        else:
            sol[random_case.name] = Solution(case_name=random_case.name, number=random_case.number,
                                             type_of_case='Einnahme')
        # nodepool.remove_node(random_case)
    return sentences


def generate(difficulty: int) -> Dict:
    solutions: Dict[str, Solution] = {}
    opt_list = {}

    earning_cases = dep.generate_all_earning_cases(
        formulation_dict=sen.EARNINGS, verbs=sen.VERBS, numbers=num.ALL)
    spending_cases = dep.generate_all_spending_cases(
        formulation_dict=sen.SPENDINGS, verbs=sen.VERBS, numbers=num.ALL, object_of_case=earning_cases[0].subject)

    pool = setup_pool('test_pool', earning_cases)
    add_all(pool, spending_cases)

    if difficulty in range(1, 11):
        sentences = pick(difficulty, pool, solutions)
    else:
        sentences = pick(5, pool, solutions)

    for val in law.ALL.values():
        map_laws(solutions, val)

    for x, key in enumerate(solutions):
        opt_list[x] = {'name': key, 'value': solutions[key].number}

    zve = calculate_zve(solutions)

    return {'sentences': sentences, 'solution': solutions, 'sum': zve, 'cases_and_sums': opt_list}


if __name__ == '__main__':
    generate(5)

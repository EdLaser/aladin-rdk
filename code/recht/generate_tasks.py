import random
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
    variation: str = var.build_variaton(case)
    if variation:
        return variation
    else:
        return "Failure in Generation."


def map_law(solution: Solution, config: Dict[str, List[str]]):
    for given_law, list_of_dep_cases in config.items():
        if solution.case_name in list_of_dep_cases:
            solution.law = given_law
        else:
            pass


def build_solution(case: Case):
    if 'WK' in case.name or 'Abschreibung' in case.name:
        return Solution(case_name=case.name, number=case.number,
                                            type_of_case='Ausgabe')
    else:
        return Solution(case_name=case.name, number=case.number,
                                        type_of_case='Einnahme')


def build_case(nodepool: NodePool, needed: str=""):
    if needed:
        # if needed is given and case found, then append it, if not append random case
        case = nodepool.pick_node(needed)
        if case:
            return case
        else:
            return Case("something went wrong", "failure", "fail", "me", 0)
    else:
        case = nodepool.pick_random_node()
        return case

# sol: Dict[str, Solution]
def pick(difficulty: int, amount: int, nodepool: NodePool,  needed_cases: List[str] = []) -> List[Case]:
    """
    Pick a node of the pool the given ammount of times.

    Parameters:
        difficulty(int): Ammount of pickings from the nodepool.
        nodepool(NodePool): The nodepool to pick the nodes from.
        sol(dict): Dictionary of the Solutions
    """
    all_cases = []
    # generated cases, len should ultimately equal the difficulty
    already_generated: List[str] = []
    
    if needed_cases:
        for needed_case in needed_cases:
            new_case = build_case(nodepool, needed=needed_case)
            all_cases.append(new_case)
        if len(needed_cases) > amount:
            return all_cases
        else:
            x = 0
            while x < amount - len(needed_cases):
                new_case = build_case(nodepool)
                # not casename not already generated
                if new_case.name in already_generated and len(already_generated) < difficulty:
                    continue
                else:
                    all_cases.append(new_case)
                    already_generated.append(new_case.name)
                    x += 1
    else:
        x = 0
        while x < amount:
            new_case = build_case(nodepool)
            if new_case.name in already_generated and len(already_generated) < difficulty:
                continue
            else:
                already_generated.append(new_case.name)
                all_cases.append(new_case)
                x += 1
        # nodepool.remove_node(random_case)
    return all_cases


def generate(difficulty: int=random.randrange(1, len(sen.EARNINGS) + len(sen.SPENDINGS)), amount: int=5, needed: List[str]=[]):
    """
    Generate all the tasks with the given Parameters.
    
    Parameters:
        difficulty(int): Number of different task types in the Task.
        amount(int): The amount of tasks generated.
        needed(List[str]): Task that the client definitely wants to be generated.
    """
    # Needs to be replaced
    DIFF_MAP = {1: random.randrange(2, 4), 2: random.randrange(5, 8), 3: random.randrange(9, 11)}

    earning_cases = dep.generate_all_earning_cases(
        formulation_dict=sen.EARNINGS, verbs=sen.VERBS, numbers=num.ALL)
    spending_cases = dep.generate_all_spending_cases(
        formulation_dict=sen.SPENDINGS, verbs=sen.VERBS, numbers=num.ALL, object_of_case=earning_cases[0].subject)

    pool = setup_pool('test_pool', earning_cases)
    add_all(pool, spending_cases)
    
    # difficulty ist here bisschen komisch
    diff_to_use = random.randrange(1, len(sen.EARNINGS) + len(sen.SPENDINGS)) if difficulty == 0 else DIFF_MAP[difficulty]
    all_cases = pick(difficulty=diff_to_use, amount=amount, nodepool=pool, needed_cases=needed)

    return all_cases


def select_options(cases: List[Case]):
    select_options_to_choose = {}
    for index, case in enumerate(cases):
        select_options_to_choose[index] = {'name': case.name, 'value': case.number}
    return select_options_to_choose

def show_all_cases():
    return { **sen.SPENDINGS, **sen.EARNINGS}


if __name__ == '__main__':
    generate(difficulty=5, amount=5)

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


def build_solution(case: Case, solutions: Dict[str, Solution]):
    if 'WK' in case.name or 'Abschreibung' in case.name:
            solutions[case.name] = Solution(case_name=case.name, number=case.number,
                                            type_of_case='Ausgabe')
    else:
        solutions[case.name] = Solution(case_name=case.name, number=case.number,
                                        type_of_case='Einnahme')


def build_case(nodepool: NodePool, already_generated: List[str], needed: str=""):
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



def pick(difficulty: int, amount: int, nodepool: NodePool, sol: Dict[str, Solution], needed_cases: List[str] = []) -> List[str]:
    """
    Pick a node of the pool the given ammount of times.

    Parameters:
        difficulty(int): Ammount of pickings from the nodepool.
        nodepool(NodePool): The nodepool to pick the nodes from.
        sol(dict): Dictionary of the Solutions
    """
    sentences = []
    already_generated: List[str] = []

    if needed_cases:
        for needed_case in needed_cases:
            sentences.append(build_sent(build_case(nodepool, already_generated=already_generated, needed=needed_case)))
        if len(needed_cases) > amount:
            return sentences
        else:
            for x in range(amount - len(needed_cases)):
                sentences.append(build_sent(build_case(nodepool, already_generated=already_generated)))
    else:
        for x in range(amount):
            sentences.append(build_sent(build_case(nodepool, already_generated=already_generated)))
        # nodepool.remove_node(random_case)
    return sentences


def generate(difficulty: int, amount: int, needed: List[str] = []) -> Dict:
    """
    Generate all the tasks with the given Parameters.
    
    Parameters:
        difficulty(int): Number of different task types in the Task.
        amount(int): The amount of tasks generated.
        needed(List[str]): Task that the client definitely wants to be generated.
    """
    solutions: Dict[str, Solution] = {}
    opt_list = {}
    amount_different_task_types = len(sen.EARNINGS) + len(sen.SPENDINGS)
    earning_cases = dep.generate_all_earning_cases(
        formulation_dict=sen.EARNINGS, verbs=sen.VERBS, numbers=num.ALL)
    spending_cases = dep.generate_all_spending_cases(
        formulation_dict=sen.SPENDINGS, verbs=sen.VERBS, numbers=num.ALL, object_of_case=earning_cases[0].subject)

    pool = setup_pool('test_pool', earning_cases)
    add_all(pool, spending_cases)

    if difficulty in range(1, amount_different_task_types):
        sentences = pick(difficulty=difficulty, amount=amount, nodepool=pool, sol=solutions, needed_cases=needed)
    else:
        sentences = pick(difficulty=5, amount=amount, nodepool=pool, sol=solutions)

    for val in law.ALL.values():
        map_laws(solutions, val)

    for x, key in enumerate(solutions):
        opt_list[x] = {'name': key, 'value': solutions[key].number}

    zve = calculate_zve(solutions)

    return {'sentences': sentences, 'solution': solutions, 'sum': zve, 'cases_and_sums': opt_list}

def show_all_cases():
    return { **sen.SPENDINGS, **sen.EARNINGS}


if __name__ == '__main__':
    generate(difficulty=5, amount=5)

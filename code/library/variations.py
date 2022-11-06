import random

from library.nodepool.case import Case

def build_variaton(case: Case) -> str:
    '''
    Build a random variation for the given case.

    Parameters:
        case(Case): The case to generate the variation for.
        parts()
    
    Returns:
       String containing the generated sentence.
    '''
    variations = []

    if case.name == 'Werbungskosten':
        return random.choice([
            f"{case.subject} {case.verb} {case.verb}"
        ])
        
    if case.name == 'Gehalt':
        return random.choice([
            f"Als {case.subject} {case.verb} {case.object} {case.number}.",
            f"{case.object} ist {case.subject} und {case.verb} {case.object}.",
            f"{case.object} {case.verb} als {case.subject} {case.number}."
        ])

    if case.name == 'Dividende':
        return random.choice([
            f"Durch eine {case.subject} {case.verb} {case.object} {case.number}.",
            f"{case.object} {case.verb} eine {case.subject} i.H.v {case.number}.",
        ])

    if case.name == 'Beteiligung':
        return random.choice([
            f"Aufgrund einer {case.subject} {case.verb} {case.object} {case.number}.",
            f"Durch eine {case.subject} {case.verb} {case.object} {case.number}.",
        ])

    if case.name == 'Vermietung':
        random.choice([
            f"Da {case.object} eine {case.subject} {case.verb} bezieht {case.object} {case.number}.",
            f"{case.object} {case.verb} eine {case.subject} und erwirtschaftet {case.number}.",
            f"Nebenbei {case.verb} {case.object} eine {case.subject} und verlangt {case.number}.",
        ])

    return ""
from library import sentenceparts as sen
from library.nodepool.case import Case
from typing import List, Dict
import random
import json
import string


def read_config(file_name: str) -> Dict:
    with open(file_name, 'r') as f:
        content = f.read()
    try:
        config_dict: Dict = json.loads(content)
        return config_dict
    finally:
        return {"error": "Parsing config failed."}


def determine_subject(case: Case, choice_of_subject: Dict[str, str], object_of_sentence: List[str]) -> bool:
    """
    Set the subject of the according case. Chooses based on gender by checking the object list for 'er' or 'sie'.

    Parameters:
        case(Case): The case the subject should be assigned to.
        choice_of_subject(dict[str, str]): Random choice of the subject out of all possible versions.
        object_of_sentence(list[str]): A list of possible objects
    Returns:
        None, just sets the cases subject.
    """
    if 'Er' in object_of_sentence and 'Er' in choice_of_subject:
        case.set_subject(choice_of_subject.get('Er'))   # type: ignore
        return True
    elif 'Sie' in object_of_sentence and 'Sie' in choice_of_subject:
        case.set_subject(choice_of_subject.get('Sie'))  # type: ignore
        return True
    else:
        return False


def generate_all_earning_cases(formulation_dict: Dict, verbs: Dict, numbers: Dict) -> List[Case]:
    """
    Takes sentence parts and transforms them to a list of case elements.

    Parameters:
        formulation_dict(dict): A dict with all formulations of the cases.
        verbs(dict): Verbs corresponding to the cases.
        numbers(dict): Given amounts for each case.
    Returns:
        cases(list): A list of all cases generated.
    """
    ch = random.choice(string.ascii_letters).upper()
    objects_for_sentence = [ch, random.choice(sen.NOUNS)]
    cases = []

    for category_name, chosen_subject in formulation_dict.items():
        case = Case()
        case.set_name(category_name)

        choice_of_subject = random.choice(chosen_subject)
        if not determine_subject(case, choice_of_subject, objects_for_sentence):
            case.set_subject(random.choice(chosen_subject))

        case.set_verb(random.choice(verbs[category_name]))

        case.set_object(random.choice(objects_for_sentence))

        case.set_number(numbers[category_name])

        cases.append(case)

    return cases


def generate_all_spending_cases(formulation_dict: Dict, verbs: Dict, numbers: Dict, object_of_case: str) -> List[Case]:
    """
    Generate all cases in which the user spends money (Werbungskosten).

    Parameters:
        formulation_dict(dict): A dict with all formulations of the cases.
        verbs(dict): Verbs corresponding to the cases.
        numbers(dict): Given amounts for each case.
        object_of_case(str): The object of the previuos cases, to set it correctly in spendings.
    Returns:
        cases(list): A list of all cases generated.
    """
    cases = []

    for category_name, chosen_wk in formulation_dict.items():
        case = Case()
        case.set_name(category_name)

        case.set_verb(random.choice(verbs[category_name]))

        case.set_object(object_of_case)

        case.set_subject(random.choice(chosen_wk))

        case.set_number(numbers['Werbungskosten'])

        cases.append(case)

    return cases
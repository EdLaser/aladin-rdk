from library import numbers as num
from library import sentenceparts as sen
from library.nodepool.case import Case
import random
import string


PARTS = ['Subject', 'Verb', 'Object']


def determine_subject(case: Case, choice_of_subject: dict[str, str], object_of_sentence: list[str]) -> bool:
    '''
    Set the subject of the according case. Chooses based on gender by checking the object list for 'er' or 'sie'.

    Parameters:
        case(Case): The case the subject should be assigned to.
        choice(dict[str, str]): Random choice of the subject out of all possible versions.
        object(lsit[str]): A list of possible objects
    Returns:
        None, just sets the cases subject.
    '''
    if 'Er' in object_of_sentence and 'Er' in choice_of_subject:
        case.set_subject(choice_of_subject.get('Er'))   # type: ignore
        return True
    elif 'Sie' in object_of_sentence and 'Sie' in choice_of_subject:
        case.set_subject(choice_of_subject.get('Sie'))  # type: ignore
        return True
    else:
        return False


def generate_all_cases(formulation_dict: dict, verbs: dict, numbers: dict) -> list:
    '''
    Takes earnings from sentence parts and transform them to a dictionary.

    Returns:
        cases(list): A list of all cases generated.
    '''
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

        case.set_number(numbers[category_name])

        cases.append(case)

    return cases

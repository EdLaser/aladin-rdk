from library import numbers as num
from library import sentenceparts as sen
from library.nodepool.case import Case
import random
import string

COMBINATIONS = {
    "COMB_1": {1: "Subject", 2: "Verb", 3: "Object"},
    "COMB_2": {1: "Verb", 2: "Subject", 3: "Object"},
    # "COMB_3": ["Subject", "Object", "Verb"]
}

PARTS = ['Subject', 'Verb', 'Object']


def determine_subject(case: Case, choice, object):
    '''Set the subject of the according case. Chooses based on gender'''
    if type(choice) is dict:
        if 'Er' in object:
            case.set_subject(choice.get('Er'))
        elif 'Sie' in object:
            case.set_subject(choice.get('Sie'))
    else:
        case.set_object(choice)


def map_cases() -> list:
    mapped = []
    ch = random.choice(string.ascii_letters).upper()
    sub = [ch, random.choice(sen.NOUNS)]
    mapped = generate_all_cases(earnings=sen.EARNINGS, spendings=sen.SPENDINGS, sent_parts=PARTS,
                                verbs=sen.VERBS, obj=sub, numbers=num.ALL)

    return mapped


def generate_all_cases(earnings: dict, spendings: dict, sent_parts: list, verbs: dict, obj: list, numbers: dict) -> list:
    '''
    Takes earnings from sentence parts and transform them to a dictionary.

    Returns:
        cases(list): A list of all cases generated.
    '''
    cases = []
    for case_name, subject_name in earnings.items():
        earning_case = Case()
        earning_case.set_name(case_name)
        
        for sentence_part in sent_parts:
            object = random.choice(obj)

            if sentence_part == 'Subject':
                choice = random.choice(subject_name)
                determine_subject(earning_case, choice, obj)

                keys_wk = list(spendings.keys())
                # wk[part] = random.choice(spendings.get(
                #    random.choice(keys_wk)))  # type: ignore

            elif sentence_part == 'Verb':
                verb_list = verbs.get(case_name)
                # wk[part] = random.choice(
                #     verbs.get('Werbungskosten'))  # type: ignore
                earning_case.set_verb(random.choice(verb_list))  # type: ignore

            elif sentence_part == 'Object':
                earning_case.set_object = object
                # wk[part] = object

        earning_case.set_number(numbers.get(case_name))
        cases.append(earning_case)
        # combs[elem + '-Werbungskosten'] = wk

    return cases


TEST = {
    'G': {'S': 'test', 'O': 'test'},
    'V': {'S': 'test', 'O': 'test'},
    'D': {'S': 'test', 'O': 'test'},
    'B': {'S': 'test', 'O': 'test'},
}

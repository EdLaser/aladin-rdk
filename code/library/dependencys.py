from library import numbers as num
from library import sentenceparts as sen
import random
import string

COMBINATIONS = {
    "COMB_1": {1: "Subject", 2: "Verb", 3: "Object"},
    "COMB_2": {1: "Verb", 2: "Subject", 3: "Object"},
    # "COMB_3": ["Subject", "Object", "Verb"]
}

PARTS = ['Subject', 'Verb', 'Object']


def set_subject(part_dict, part, choice, object):
    if type(choice) is dict:
        if 'Er' in object:
            part_dict[part] = choice.get('Er')
        elif 'Sie' in object:
            part_dict[part] = choice.get('Sie')
    else:
        part_dict[part] = choice


def map_cases() -> dict:
    mapped = {}
    ch = random.choice(string.ascii_letters).upper()
    sub = [ch, random.choice(sen.NOUNS)]
    mapped = generate_all_cases(earnings=sen.EARNINGS, spendings=sen.SPENDINGS, sent_parts=PARTS,
                                verbs=sen.VERBS, obj=sub, numbers=num.ALL)

    return mapped


def generate_all_cases(earnings: dict, spendings: dict, sent_parts: list, verbs: dict, obj: list, numbers: dict) -> dict:
    combs = {}
    for case_name, subject_name in earnings.items():
        earning_case = {}
        wk = {}
        for sentence_part in sent_parts:
            object = random.choice(obj)

            if sentence_part == 'Subject':
                choice = random.choice(subject_name)
                set_subject(earning_case, sentence_part, choice, obj)

                keys_wk = list(spendings.keys())
                # wk[part] = random.choice(spendings.get(
                #    random.choice(keys_wk)))  # type: ignore

            elif sentence_part == 'Verb':
                word_list = verbs.get(case_name)
                # wk[part] = random.choice(
                #     verbs.get('Werbungskosten'))  # type: ignore
                earning_case[part] = random.choice(word_list)  # type: ignore

            elif sentence_part == 'Object':
                earning_case[sentence_part] = object
                # wk[part] = object

        earning_case['Number'] = numbers.get(case_name)

        combs[case_name] = earning_case
        # combs[elem + '-Werbungskosten'] = wk

    return combs


TEST = {
    'G': {'S': 'test', 'O': 'test'},
    'V': {'S': 'test', 'O': 'test'},
    'D': {'S': 'test', 'O': 'test'},
    'B': {'S': 'test', 'O': 'test'},
}

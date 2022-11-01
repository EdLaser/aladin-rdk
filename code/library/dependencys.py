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


def map_parts():
    mapped = {}
    ch = random.choice(string.ascii_letters).upper()
    sub = [ch, random.choice(sen.NOUNS)]
    mapped = generate_combs(earnings=sen.EARNINGS, spendings=sen.SPENDINGS, sent_parts=PARTS,
                            verbs=sen.VERBS, obj=sub, numbers=num.ALL)

    return mapped


def generate_combs(earnings: dict, spendings: dict, sent_parts: list, verbs: dict, obj: list, numbers: dict):
    combs = {}
    for elem, value in earnings.items():
        part_dict = {}
        wk = {}
        for part in sent_parts:
            object = random.choice(obj)

            if part == 'Subject':
                choice = random.choice(value)
                set_subject(part_dict, part, choice, obj)
                
                keys_wk = list(spendings.keys())
                wk[part] = random.choice(spendings.get(random.choice(keys_wk)))  # type: ignore

            elif part == 'Verb':
                word_list = verbs.get(elem)
                wk[part] = random.choice(verbs.get('Werbungskosten'))  # type: ignore
                part_dict[part] = random.choice(word_list)  # type: ignore

            elif part == 'Object':
                part_dict[part] = object
                wk[part] = object

        part_dict['Number'] = numbers.get(elem)

        print(wk)
        combs[elem] = part_dict
        combs['Werbungskosten'] = wk

    return combs


TEST = {
    'G': {'S': 'test', 'O': 'test'},
    'V': {'S': 'test', 'O': 'test'},
    'D': {'S': 'test', 'O': 'test'},
    'B': {'S': 'test', 'O': 'test'},
}

from library import earnings
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


def map_parts():
    mapped = {}
    ch = random.choice(string.ascii_letters).upper()
    sub = [ch, random.choice(sen.NOUNS)]
    mapped = generate_combs(formulation=sen.ALL, sent_parts=PARTS,
                            verbs=sen.VERBS, obj=sub, numbers=num.ALL)

    return mapped


def generate_combs(formulation: dict, sent_parts: list, verbs: list, obj: list, numbers: dict):
    combs = {}
    for elem, value in formulation.items():
        print(elem, value)
        part_dict = {}
        for part in sent_parts:
            object = random.choice(obj)
            if part == 'Subject':
                choice = random.choice(value)
                if isinstance(choice, dict):
                    if 'Er' in object:
                        part_dict[part] = choice.get('Er')
                    if 'Sie' in object:
                        part_dict[part] = choice.get('Sie')
                else:
                    part_dict[part] = random.choice(value)
            elif part == 'Verb':
                part_dict[part] = random.choice(verbs)
            elif part == 'Object':
                part_dict[part] = object
        part_dict['Number'] = numbers.get(elem)
        combs[elem] = part_dict

    return combs


TEST = {
    'G': {'S': 'test', 'O': 'test'},
    'V': {'S': 'test', 'O': 'test'},
    'D': {'S': 'test', 'O': 'test'},
    'B': {'S': 'test', 'O': 'test'},
}

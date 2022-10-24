import imp
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

CONJUNCTION = {
    'COMB_1': [''],
    'COMB_2': ['']
    }

def map_parts():
    mapped = {}
    ch = random.choice(string.ascii_letters).upper()
    for k, v in COMBINATIONS.items():
        mapped[k] = generate_combs(formulation=sen.ALL, sent_parts=v, verbs=sen.VERBS, obj=ch, numbers=num.ALL)
    
    return mapped
            

def generate_combs(formulation: dict, sent_parts: dict, verbs: list, obj: list, numbers: dict):
    combs = {}
    for elem, value in formulation.items():
        part_dict = {}
        for key, val in sent_parts.items():
            if val == 'Subject':
                part_dict[key] = random.choice(value)
            elif val == 'Verb':
                part_dict[key] = random.choice(verbs)
            elif val == 'Object':
                part_dict[key] = obj
            part_dict['Number'] = numbers.get(elem)
        combs[elem] = part_dict
    
    return combs


TEST = {
    'COMB_1': {
        'G': {'S': 'test', 'O': 'test'},
        'V': {'S': 'test', 'O': 'test'},
        'D': {'S': 'test', 'O': 'test'},
        'B': {'S': 'test', 'O': 'test'},
    },
    'COMB_2': {
        'G': {'S': 'test', 'O': 'test'},
        'V': {'S': 'test', 'O': 'test'},
        'D': {'S': 'test', 'O': 'test'},
        'B': {'S': 'test', 'O': 'test'},
    }
}
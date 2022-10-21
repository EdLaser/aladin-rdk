import imp
from library import earnings
from library import spendings
from library import sentenceparts as sen
import random
import string

COMBINATIONS = {"COMB_1": ["Subject", "Verb", "Object"],
                "COMB_2": ["Verb", "Subject", "Object"],
                # "COMB_3": ["Subject", "Object", "Verb"]
                }

def map_parts():
    mapped = {}
    for k, v in COMBINATIONS.items():
        mapped[k] = generate_combs(sen.ALL, v, sen.VERBS, random.choice(string.ascii_letters).upper())
    
    return mapped
            

def generate_combs(formulation, sent_parts, verbs, obj):
    combs = {}
    for elem, value in formulation.items():
        part_dict = {}
        print(value)
        for val in sent_parts:
            if val == 'Subject':
                part_dict[val] = random.choice(value)
            elif val == 'Verb':
                part_dict[val] = random.choice(verbs)
            elif val == 'Object':
                part_dict[val] = obj
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
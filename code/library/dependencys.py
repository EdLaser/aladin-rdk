import earnings
import spendings
import numbers

COMBINATIONS = {"COMB_1": ["Subjekt", "Verb", "Object"],
                "COMB_2": ["Verb", "Subject", "Object"],
                "COMB_3": ["Subject", "Object", "Verb"]}


def generate_number_dep():
    NUMBERS = {}
    for earn in earnings.ALL:
        for key, num in numbers.ALL.items():
            if earn is key:
                NUMBERS[earn] = num
            else:
                pass
    return NUMBERS
